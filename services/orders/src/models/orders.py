from pydantic import BaseModel, confloat


class Location(BaseModel):
    lat: confloat(ge=-90, le=90)
    lon: confloat(ge=-180, le=180)

class OrdersRequest(BaseModel):
    destination_from: Location
    destination_to: Location