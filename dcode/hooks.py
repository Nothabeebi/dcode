from . import __version__ as app_version

app_name = "dcode"
app_title = "Dcode"
app_publisher = "Habeeb Abdullah"
app_description = "Theme"
app_email = "habeeb@zoserp.com"
app_license = "MIT"

fixtures = ["Web Page"]
base_template = "dcode/templates/base.html"


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dcode/css/dcode.css"
# app_include_js = "/assets/dcode/js/dcode.js"

# include js, css files in header of web template
# web_include_css = ["/assets/dcode/css/animate.css","/assets/dcode/css/slick.css",
#                 "/assets/dcode/css/materialdesignicons.min.css",
#                 "/assets/dcode/css/style.css","/assets/dcode/css/line-awesome.min.css",
#                 "/assets/dcode/css/fontawesome.min.css","/assets/dcode/css/default-color.css"]
#web_include_js = ["/assets/dcode/js/dcode.js","/assets/dcode/js/appear.js"]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dcode/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dcode.utils.jinja_methods",
# 	"filters": "dcode.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dcode.install.before_install"
# after_install = "dcode.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dcode.uninstall.before_uninstall"
# after_uninstall = "dcode.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dcode.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dcode.tasks.all"
# 	],
# 	"daily": [
# 		"dcode.tasks.daily"
# 	],
# 	"hourly": [
# 		"dcode.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dcode.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dcode.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dcode.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dcode.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dcode.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dcode.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
