odoo.define('SchoolManagementSystem.sidebar', function (require) {
    "use strict";

    const WebClient = require('web.WebClient');

    WebClient.include({
        show_application(app_id) {
            return this._super.apply(this, arguments).then(() => {
                const app = this.menu.get_app(app_id);
                const isSchoolApp = app && app.xmlid === 'menu_school';

                // Remove any existing sidebar
                const existingSidebar = document.getElementById('school_sidebar');
                if (existingSidebar) existingSidebar.remove();
                document.querySelector('.o_action_manager').style.marginLeft = '0';

                if (isSchoolApp) {
                    // Inject Sidebar
                    const $sidebar = document.createElement('div');
                    $sidebar.id = 'school_sidebar';
                    $sidebar.innerHTML = `
                        <a href="#">Dashboard</a>
                        <a href="#">Transport</a>
                        <a href="#">Users</a>
                        <a href="#">Alumni</a>
                        <a href="#">Academics</a>
                        <a href="#">Exams</a>
                        <a href="#">Accounting</a>
                        <a href="#">Online Courses</a>
                    `;
                    document.body.appendChild($sidebar);

                    // Adjust main content
                    const actionManager = document.querySelector('.o_action_manager');
                    if (actionManager) {
                        actionManager.style.marginLeft = '200px';
                    }
                }
            });
        },
    });
});
