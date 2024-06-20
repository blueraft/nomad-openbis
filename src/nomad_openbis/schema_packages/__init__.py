from nomad.config.models.plugins import SchemaPackageEntryPoint


class OpenbisEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_openbis.schema_packages.openbis import m_package
 
        return m_package


openbis = OpenbisEntryPoint(
    name='Openbis',
    description='Schema package defined using the new plugin mechanism.',
)
