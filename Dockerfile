FROM odoo:17.0

USER root

COPY ./addons /mnt/extra-addons

COPY ./config/odoo.conf /etc/odoo/odoo.conf

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8069/web/health || exit 1

USER odoo

EXPOSE 8069