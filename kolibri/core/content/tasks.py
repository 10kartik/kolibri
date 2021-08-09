import os

from django.core.management import call_command

from kolibri.core.content.permissions import CanManageContent
from kolibri.core.content.task_validators import get_channel_name
from kolibri.core.content.task_validators import validate_startdiskexport
from kolibri.core.content.task_validators import validate_startchannelupdate
from kolibri.core.content.task_validators import validate_startdiskcontentimport
from kolibri.core.content.task_validators import validate_startremotechannelimport
from kolibri.core.content.task_validators import validate_startremotecontentimport
from kolibri.core.content.utils.paths import get_content_database_file_path
from kolibri.core.tasks.decorators import register_task
from kolibri.core.tasks.exceptions import UserCancelledError
from kolibri.core.tasks.utils import get_current_job


@register_task(
    validator=validate_startdiskcontentimport,
    cancellable=True,
    track_progress=True,
    permission_classes=[CanManageContent],
)
def startdiskcontentimport(**kwargs):
    call_command(
        "importcontent",
        "disk",
        kwargs["channel_id"],
        kwargs["datafolder"],
        drive_id=kwargs["drive_id"],
        node_ids=kwargs["node_ids"],
        exclude_node_ids=kwargs["exclude_node_ids"],
    )


@register_task(
    validator=validate_startchannelupdate,
    cancellable=True,
    track_progress=True,
    permission_classes=[CanManageContent],
)
def startchannelupdate(**kwargs):
    if kwargs["sourcetype"] == "remote":
        call_command(
            "importchannel",
            "network",
            kwargs["channel_id"],
            baseurl=kwargs["baseurl"],
            update_progress=kwargs["update_progress"],
            check_for_cancel=kwargs["check_for_cancel"],
        )

        # Make some real-time updates to the metadata
        job = get_current_job()

        # Signal to UI that the DB-downloading step is done so it knows to display
        # progress correctly
        job.update_progress(0, 1.0)
        job.extra_metadata["database_ready"] = True

        # Add the channel name if it wasn't added initially
        if job and job.extra_metadata.get("channel_name", "") == "":
            job.extra_metadata["channel_name"] = get_channel_name(kwargs["channel_id"])

        job.save_meta()

        call_command(
            "importcontent",
            "network",
            kwargs["channel_id"],
            baseurl=kwargs["baseurl"],
            peer_id=kwargs["peer_id"],
            node_ids=kwargs["node_ids"],
            exclude_node_ids=kwargs["exclude_node_ids"],
            import_updates=kwargs["is_updating"],
            update_progress=kwargs["update_progress"],
            check_for_cancel=kwargs["check_for_cancel"],
        )
    elif kwargs["sourcetype"] == "local":
        call_command(
            "importchannel",
            "disk",
            kwargs["channel_id"],
            kwargs["directory"],
            update_progress=kwargs["update_progress"],
            check_for_cancel=kwargs["check_for_cancel"],
        )

        # Make some real-time updates to the metadata
        job = get_current_job()

        # Signal to UI that the DB-downloading step is done so it knows to display
        # progress correctly
        job.update_progress(0, 1.0)
        job.extra_metadata["database_ready"] = True

        # Add the channel name if it wasn't added initially
        if job and job.extra_metadata.get("channel_name", "") == "":
            job.extra_metadata["channel_name"] = get_channel_name(kwargs["channel_id"])

        job.save_meta()

        # Skip importcontent step if updating and no nodes have changed
        if (
            kwargs["is_updating"]
            and (kwargs["node_ids"] is not None)
            and len(kwargs["node_ids"]) == 0
        ):
            pass
        else:
            call_command(
                "importcontent",
                "disk",
                kwargs["channel_id"],
                kwargs["directory"],
                drive_id=kwargs["drive_id"],
                node_ids=kwargs["node_ids"],
                exclude_node_ids=kwargs["exclude_node_ids"],
                update_progress=kwargs["update_progress"],
                check_for_cancel=kwargs["check_for_cancel"],
            )


@register_task(
    validator=validate_startremotechannelimport,
    cancellable=True,
    permission_classes=[CanManageContent],
)
def startremotechannelimport(**kwargs):
    call_command(
        "importchannel",
        "network",
        kwargs["channel_id"],
        baseurl=kwargs["baseurl"],
        peer_id=kwargs["peer_id"],
    )


@register_task(
    validator=validate_startremotecontentimport,
    track_progress=True,
    cancellable=True,
    permission_classes=[CanManageContent],
)
def startremotecontentimport(**kwargs):
    call_command(
        "importcontent",
        "network",
        kwargs["channel_id"],
        baseurl=kwargs["baseurl"],
        peer_id=kwargs["peer_id"],
        node_ids=kwargs["node_ids"],
        exclude_node_ids=kwargs["exclude_node_ids"],
    )


@register_task(
    validator=validate_startdiskexport,
    track_progress=True,
    cancellable=True,
    permission_classes=[CanManageContent],
)
def startdiskexport(**kwargs):
    """
    Export a channel to a local drive, and copy content to the drive.
    """
    from kolibri.core.content.utils.channels import get_mounted_drive_by_id

    drive = get_mounted_drive_by_id(kwargs["drive_id"])

    call_command(
        "exportchannel",
        kwargs["channel_id"],
        drive.datafolder,
        update_progress=kwargs["update_progress"],
        check_for_cancel=kwargs["check_for_cancel"],
    )
    try:
        call_command(
            "exportcontent",
            kwargs["channel_id"],
            drive.datafolder,
            node_ids=kwargs["node_ids"],
            exclude_node_ids=kwargs["exclude_node_ids"],
            update_progress=kwargs["update_progress"],
            check_for_cancel=kwargs["check_for_cancel"],
        )
    except UserCancelledError:
        try:
            os.remove(
                get_content_database_file_path(
                    kwargs["channel_id"], datafolder=drive.datafolder
                )
            )
        except OSError:
            pass
        raise
