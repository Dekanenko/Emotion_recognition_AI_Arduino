from pydantic import BaseModel, conint

class RGBColor(BaseModel):
    r: conint(ge=0, le=255)
    g: conint(ge=0, le=255)
    b: conint(ge=0, le=255)

    def __str__(self):
        return f"R: {self.r} | G: {self.g} | B: {self.b}"