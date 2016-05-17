"""
No mocks! Ensure that hooks work by extending them and overriding methods with
emulated side-effects.
"""

from __future__ import absolute_import, print_function, unicode_literals

from django.test.testcases import TestCase

from .. import hooks
from .base import TestHookMixin


class _WebpackBundleHookSwappedOut(hooks.WebpackBundleHook):
    unique_slug = "i_get_swapped_out"


class _WebpackBundleHookInheritor(_WebpackBundleHookSwappedOut):

    unique_slug = "i_get_swapped_in"

    class Meta:
        replace_parent = True


class _FrontEndCoreHook(hooks.FrontEndCoreHook):
    unique_slug = "im_a_core_hook"

    class Meta:
        replace_parent = True


class _FrontEndASyncHook(TestHookMixin, hooks.FrontEndASyncHook):
    unique_slug = "im_an_async_hook"

    events = {
        'some_weird_event_we_are_going_to_look_for': 'value'
    }


class WebpackBundleHookTestCase(TestCase):

    def test_replacement(self):
        """
        Test that the parent of ``_WebpackBundleHookInheritor`` is no longer in
        the registry. Other tests depend on this.
        """
        registered_types = [
            type(hook) for hook in hooks.WebpackBundleHook().registered_hooks
        ]

        # Assert that
        self.assertNotIn(
            _WebpackBundleHookSwappedOut,
            registered_types
        )
        self.assertIn(
            _WebpackBundleHookInheritor,
            registered_types
        )

    def test_sync_hook(self):

        for hook in hooks.FrontEndAssetHook().registered_hooks:
            if type(hook) is _FrontEndASyncHook:
                for event_key in _FrontEndASyncHook.events.keys():
                    self.assertIn(
                        event_key,
                        hook.render_to_html(),
                    )
