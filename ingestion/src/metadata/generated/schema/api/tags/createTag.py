# generated by datamodel-codegen:
#   filename:  schema/api/tags/createTag.json
#   timestamp: 2021-11-11T08:56:06+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...entity.tags import tagCategory


class CreateTagEntityRequest(BaseModel):
    name: tagCategory.TagName
    description: str = Field(..., description='Unique name of the tag category')
    associatedTags: Optional[List[str]] = Field(
        None, description='Fully qualified names of tags associated with this tag'
    )
