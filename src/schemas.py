from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Language(BaseModel):
    code: str
    name: str
    native: str

class Timezone(BaseModel):
    id: str
    current_time: datetime
    gmt_offset: int
    code: str
    is_daylight_saving: bool

class Currency(BaseModel):
    code: str
    name: str
    plural: str
    symbol: str
    symbol_name: str

class IPConnection(BaseModel):
    asn: int
    isp: str


class IPLocation(BaseModel):
    geoname_id: Optional[int] = None
    capital: Optional[str] = None
    languages: Optional[List[Language]] = None
    country_flag: Optional[str] = None
    country_flag_emoji: Optional[str] = None
    country_flag_emoji_unicode: Optional[str] = None
    calling_code: Optional[str] = None
    is_eu: Optional[bool] = None

class IPSecurity(BaseModel):
    is_proxy: Optional[bool] = None
    proxy_type: Optional[str] = None
    is_crawler: Optional[bool] = None
    crawler_name: Optional[str] = None
    crawler_type: Optional[str] = None
    is_tor: Optional[bool] = None
    threat_level: Optional[str] = None
    threat_types: Optional[List[str]] = None

class IPInformation(BaseModel):
    ip: str
    hostname: Optional[str] = None
    type: str
    continent_code: Optional[str] = None
    continent_name: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    region_code: Optional[str] = None
    region_name: Optional[str] = None
    city: Optional[str] = None
    zip: Optional[str] = None
    latitude: float
    longitude: float
    location: IPLocation
    time_zone: Optional[Timezone] = None
    currency: Optional[Currency] = None
    connection: Optional[IPConnection] = None
    security: Optional[IPSecurity] = None
