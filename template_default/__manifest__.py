##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'template3',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Test for v13 CE",
    'author': "jeo Software",
    'website': 'https://github.com/sebacorreacalamuchita/cl-template3',
    'license': 'AGPL-3',
    'depends': [
        'standard_depends_ce'
        ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # Config to write in odoo.conf
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/sebacorreacalamuchita/cl-template3',

        # OCA
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/crm oca-crm',
        'https://github.com/OCA/project oca-project',
        'https://github.com/OCA/web oca-web',
        'https://github.com/OCA/server-backend oca-server-backend',
        'https://github.com/OCA/business-requirement oca-business-requirement',

        # ingadhoc
        'https://github.com/ingadhoc/product ingadhoc-product',

        # Cambiamos por el de filoquin
        #'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina',
        'https://github.com/filoquin/odoo-argentina-ce.git -b 13.0_qr',

        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous',
        'https://github.com/ingadhoc/website ingadhoc-website',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/odoo-public-administration ingadhoc-odoo-public-administration',
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale',
        'https://github.com/ingadhoc/partner ingadhoc-partner',
        'https://github.com/ingadhoc/odoo-argentina-ce ingadhoc-odoo-argentina-ce',
        'https://github.com/ingadhoc/hr ingadhoc-hr',
        'https://github.com/ingadhoc/project ingadhoc-project',

        # Odoomates
        'https://github.com/odoomates/odooapps odoomates-odooapps',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
