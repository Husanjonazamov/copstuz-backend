from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "icon": "group",
                "link": reverse_lazy("admin:api_botusermodel_changelist"),
            },
        ],
    },
    {
        "title": _("Qo'shimchalar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Sklad Manzili"),
                "icon": "location_on",
                "link": reverse_lazy("admin:api_cargolocationmodel_changelist"),
            },
            {
                "title": _("Filiallar"),
                "icon": "apartment",
                "link": reverse_lazy("admin:api_branchmodel_changelist"),
            },
            {
                "title": _("Excel fayl"),
                "icon": "apartment",
                "link": reverse_lazy("admin:api_excelfilemodel_changelist"),
            },
        ],
    },
]
