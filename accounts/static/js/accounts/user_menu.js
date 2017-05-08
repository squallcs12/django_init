jQuery(function () {
    var $ = jQuery;

    var opened_links = [];
    var opened_menu = $.cookie("user_openned_menu");
    if (opened_menu) {
        opened_links = opened_menu.split(";");
    }

    var $userMenu = $('#userMenu');
    var $menuHeadings = $userMenu.find('.panel-heading a');
    $menuHeadings.each(function () {
        var this_link = $(this).prop("href").split("#")[1];
        if (opened_links.indexOf(this_link) !== -1) {
            $(this).click();
        }
    });

    $menuHeadings.on('click', function (e) {
        var this_link = $(this).prop("href").split("#")[1];

        var found = opened_links.indexOf(this_link);

        if (found === -1) {
            opened_links.push(this_link);
        } else {
            opened_links.splice(found, 1);
        }
        opened_menu = opened_links.join(";");

        var date = new Date();
        date.setTime(date.getTime() + (8 * 60 * 60 * 1000));
        $.cookie("user_openned_menu", opened_menu, {path: '/', expires: date});
    });

    $userMenu.find('.top-buttons a').on('click', function (e) {
        var click = $(this).data("click");
        if (click === "expand") {
            $menuHeadings.each(function () {
                var this_link = $(this).prop("href").split("#")[1];
                if (opened_links.indexOf(this_link) === -1) {
                    $(this).click();
                }
            });
        } else {
            $menuHeadings.each(function () {
                var this_link = $(this).prop("href").split("#")[1];
                if (opened_links.indexOf(this_link) !== -1) {
                    $(this).click();
                }
            });
        }
        e.preventDefault();
        return false;
    });
});
