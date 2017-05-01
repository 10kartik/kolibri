Facility Admin
===============

.. literalinclude:: manage_users.rst







9999999999999999999999999999999999999999999999999999999



































Manage Users
------------

You can search for, filter, add, and edit user accounts in Kolibri from the **Users** tab in your **Manage** dashboard.

.. image:: img/manage_users.png
  :alt: manage users

Kolibri User Roles
~~~~~~~~~~~~~~~~~~

Kolibri users can have different roles with respective access to features:

* **Learners** can:
  
  * View content and have their progress tracked
* **Coaches** can:
  
  * View content and have their progress tracked
  * View *Coach Reports* to track progress of other users and usage stats for individual exercises
* **Admins** can:

  * View content and have their progress tracked
  * View *Coach Reports* to track progress of other users and usage stats for individual exercises
  * Create/Edit/Delete other **Admins** and **Learners**
  * Create/Edit/Delete *Classes* and *Groups* and enroll users in them
  * Export *Detail* and *Summary* logs usage data
* **Device Owners** can:

  * View content
  * View *Coach Reports* to track progress of other users and usage stats for individual exercises
  * Create/Edit/Delete other **Admins** and **Learners**
  * Create/Edit/Delete *Classes* and *Groups* and enroll users in them
  * Export *Detail* and *Summary* logs usage data
  * Import/Export content


.. note::
  To manage Kolibri users you must be logged-in as **Device Owner** or **Admin**.


Create a New User Account
~~~~~~~~~~~~~~~~~~~~~~~~~

To create a new user account, follow these steps.

#. Click **Add new** button.
#. Fill in the required information (name, username, password).
#. Select user profile (*Admin*, *Coach* or *Learner*). 
#. Click **Create account** to add the new user.

.. image:: img/add_new_account.png
  :alt: add new account form


Select Users by Type
~~~~~~~~~~~~~~~~~~~~

#. Click **All users** selector to display user types. 
#. Toggle between options to filter the user roster according to type, or leave it as **All users** to display all.

.. image:: img/select_users.png
  :alt: select users


Edit User’s Account
~~~~~~~~~~~~~~~~~~~

To edit username or the full name account, follow these steps.

#. Click on the **Edit** button (pencil icon) next to the user’s name.
#. Edit **Full name** or **Username** in the **Edit account info** window. 
#. Click **Confirm** to update the edited information or **Cancel** to exit without saving.

.. image:: img/edit_account_info.png
  :alt: edit account info form


Reset User’s Password
*********************

#. Click **Reset password** in the **Edit account info** window. 
#. Enter the new password in both fields.
#. Click **Save** to confirm or **Back** to exit without changing the password.

.. image:: img/edit_password.png
  :alt: edit password form


Delete User’s Account
*********************

#. Click **Delete User** in the **Edit Account Info** window.
#. Click **Yes** to confirm or **No** to exit without deleting the account.

.. image:: img/delete_account_confirm.png
  :alt: confirm delete account


Manage Classes
--------------

.. note::
  To manage Kolibri classes and groups you must be logged-in as **Device Owner** or **Admin**.

You can view, create and delete classes and learner groups, as well as search, filter and enroll Kolibri users in them, using the **Classes** tab in your **Manage** dashboard. Default view displays the list of all classes in your facility, with the number of enrolled users and assigned coaches for each class. 

.. image:: img/classes.png
  :alt: manage classes


Add New Class
~~~~~~~~~~~~~

To add a new class, follow these steps.

#. Click **Add new class** button.
#. Fill in the class name. 
#. Click **Create** to add the new class or **Cancel** to exit.
#. Click **Add Users to Class** to :ref:`select_users_class` or **Not now** to simply create the new class. 

Edit Class
~~~~~~~~~~~~~

To edit class, follow these steps.

#. Click the desired class name from the list.
#. Fill in the class name. 
#. Click **Create** to add the new class or **Cancel** to exit.
#. Click **Add Users to Class** to :ref:`select_users_class` or **Not now** to simply create the new class. 


Delete Class
~~~~~~~~~~~~

#. Click **Delete Class** button for the chosen class.
#. Click **Delete** to confirm or **Cancel** to exit without deleting the class. 

.. image:: img/delete_class.png
  :alt: delete class

.. note::
  Users enrolled in the class you are deleting will not be removed from the database.


Edit Class
~~~~~~~~~~

To edit a class select it from the default view in the **Classes** tab. In this vew you can organize users in groups, assign roles, add and remove the users from the class. 


Add Learner Group
~~~~~~~~~~~~~~~~~

.. image:: img/learner_groups.png
  :alt: learner groups list

To add a new learner group, follow these steps.

#. Click **+ New Learner Group** button.
#. Fill in the group name in the text field. 
#. Click **Create New Learner Group** button or **Cancel** to exit.

.. image:: img/create_learner_group.png
  :alt: create learner group


Delete Learner Group
~~~~~~~~~~~~~~~~~~~~

#. Click **Delete Group** button for the chosen group.
#. Click **Yes** to confirm or **No** to exit without deleting the group.

.. image:: img/delete_learner_group.png
  :alt: delete learner group

.. note::
  Users enrolled in the group you are deleting will be assigned the status *Ungrouped*, but will not be removed from the database.


View and edit class users
~~~~~~~~~~~~~~~~~~~~~~~~~

Below the **Learner Groups** you can view the list of all the users, both learners and coaches, see their roles and groups they are assigned to.

.. image:: img/learners_coaches.png
  :alt: list view of class users 

* Use the search field on top to quickly find a specific user.
* You can sort users using arrow selectors in each column header.
* Change the user role from **Learner** to **Coach** with the *Role* selector.
* Select and assign the group to each user from the *Group* dropdown selector.

.. note::
  Roles are *class-specific*, not *user-specific*: user can be a **Coach** in Class 1, and a **Learner** in Class 2

.. _select_users_class:

Select users to enroll to class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: img/add_users_to_class.png
  :alt: add users to the newly created class

* List contains all the users currently not enrolled for the given class.
* You can sort user list alphabetically and/or search for a specific user by name.
* Use the checkbox to select all the users you want to assign to class.
* Use the option *Create & Enroll a brand new user* for users who were not created previously.
* Click **Review & Save** button to finish enrolling users or **Cancel** to go back to user list.

.. image:: img/create_enroll.png
  :alt: create and enroll a brand new user


Remove users from class
~~~~~~~~~~~~~~~~~~~~~~~

#. Click **Remove** button for the chosen user.
#. Click **Remove** to confirm or **Cancel** to exit without removing the user.

.. image:: img/remove_user_from_class.png
  :alt: remove user from class

.. note::
  Users removed from the class will not be deleted from the database, and you can still access their account from the **Users** tab in the **Manage** dashboard.


Manage Data
-----------

.. note::
  To manage Kolibri usage data you must be logged-in as **Device Owner** or **Admin**. 

You can download Kolibri *Detail* and *Summary* logs usage data and export in the CSV format from the **Data** tab in your **Manage** dashboard.

.. image:: img/export_usage_data.png
  :alt: options for exporting usage data 


Manage Content
--------------

.. note::
  To manage Kolibri content you must be logged-in as **Device Owner**. 

Kolibri **Content Channel** is a collection of educational resources (video, audio or document files) prepared and organized by the content curator for their use in Kolibri. Each Kolibri **Content Channel** has its own *Content Channel ID* on `Kolibri content curation server <https://contentworkshop.learningequality.org/accounts/login/>`_ database that you will receive from the content curator who assembled the channel.

You can import and export **Content Channels** for Kolibri in the **Content** tab.

.. image:: img/manage_content.png
  :alt: manage content page with list of available channels



Import Content Channel to Kolibri
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To import **Content Channel** to Kolibri, follow these steps.

#. Click **Import** button in **My Channels** pane.
#. Choose the source option (*Internet* or *Local Drives*).

.. image:: img/import_choose_source.png
  :alt: choose source for importing content


Import Content Channel from the Internet
****************************************

#. Choose option for *Internet*.
#. Enter *Content Database ID* for the desired channel from the content curation server. 
#. Click **Import** button.
#. Wait for the content to be downloaded and appear under the **My Channels** heading.

.. image:: img/import_internet.png
  :alt: enter content id to import channel from internet

.. image:: img/import_CC.png
  :alt: 


Import Content Channel from a Local Drive
*****************************************

#. Choose option for *Local Drives*.
#. Kolibri will automatically detect the drive(s) with available content files. 
#. Click **Import** button.
#. Wait for the content to be imported and appear under the **My Channels** heading.

.. image:: img/import_local_drive.png
  :alt: import channel from detected local drive

.. note::
  If the local drive is not detected, try re-inserting the storage device (USB key or external hard disk) and pressing the button **Refresh**.


Export from Kolibri to Local Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Click **Export** button in **My Channels** pane.
#. Select the local drive where you wish to export **Kolibri** content.
#. Click **Export** button.

.. image:: img/export_local_drive.png
  :alt: export channel to detected local drive

.. image:: img/export_local_drive2.png
  :alt: 


Get support
-----------

If you want to contact **Learning Equality** Support team to report an issue, or share your experience about using Kolibri, please register at our `Community Forums <https://community.learningequality.org/>`_.

Once you register on our forums, please read the the first two pinned topics (*Welcome to LE’s Support Community* and *How do I post to this forum?* ) 

You can add the new topic with the **+ New Topic** button on the right. Make sure to select the **Kolibri** category in the **Create a New Topic** window so it’s easier to classify and respond to.

.. image:: img/community_forums.png
  :alt: add new topic on community forums
