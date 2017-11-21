
import base_section

class ComputeFeatureEnabled(base_section.BaseSection):

    name = "compute-feature-enabled"
    options = [
        'api_extensions',
        'attach_encrypted_volume',
        'block_migrate_cinder_iscsi',
        'block_migration_for_live_migration',
        'change_password',
        'cold_migration',
        'config_drive',
        'console_output',
        'disk_config',
        'enable_instance_password',
        'interface_attach',
        'live_migrate_back_and_forth',
        'live_migration',
        'metadata_service',
        'nova_cert',
        'pause',
        'personality',
        'rdp_console',
        'rescue',
        'resize',
        'scheduler_available_filters',
        'serial_console',
        'shelve',
        'snapshot',
        'spice_console',
        'suspend',
        'swap_volume',
        'vnc_console',
    ]


    @property
    def api_extensions(self):
        pass

    @property
    def attach_encrypted_volume(self):
        pass

    @property
    def block_migrate_cinder_iscsi(self):
        pass

    @property
    def block_migration_for_live_migration(self):
        pass

    @property
    def change_password(self):
        pass

    @property
    def cold_migration(self):
        pass

    @property
    def config_drive(self):
        pass

    @property
    def console_output(self):
        pass

    @property
    def disk_config(self):
        pass

    @property
    def enable_instance_password(self):
        pass

    @property
    def interface_attach(self):
        pass

    @property
    def live_migrate_back_and_forth(self):
        pass

    @property
    def live_migration(self):
        pass

    @property
    def metadata_service(self):
        pass

    @property
    def nova_cert(self):
        pass

    @property
    def pause(self):
        pass

    @property
    def personality(self):
        pass

    @property
    def rdp_console(self):
        pass

    @property
    def rescue(self):
        pass

    @property
    def resize(self):
        pass

    @property
    def scheduler_available_filters(self):
        pass

    @property
    def serial_console(self):
        pass

    @property
    def shelve(self):
        pass

    @property
    def snapshot(self):
        pass

    @property
    def spice_console(self):
        pass

    @property
    def suspend(self):
        pass

    @property
    def swap_volume(self):
        pass

    @property
    def vnc_console(self):
        pass
