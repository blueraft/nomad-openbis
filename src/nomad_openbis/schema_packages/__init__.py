from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class OpenbisEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_openbis.schema_packages.openbis import m_package
 
        return m_package


openbis = OpenbisEntryPoint(
    name='Openbis',
    description='Schema package defined using the new plugin mechanism.',
)
