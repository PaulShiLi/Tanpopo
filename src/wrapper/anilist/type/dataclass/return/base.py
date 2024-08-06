from dataclasses import dataclass
from typing import Optional

@dataclass
class Page:
    total: Optional[int]
    currentPage: Optional[int]
    lastPage: Optional[int]
    hasNextPage: Optional[bool]
    perPage: Optional[int]

######################
# Media Types #
@dataclass
class Title:
    romaji: Optional[str]
    english: Optional[str]
    native: Optional[str]

@dataclass
class Date:
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]

@dataclass
class Dates:
    startDate: Optional[Date]
    endDate: Optional[Date]

@dataclass
class Img:
    large: Optional[str]
    medium: Optional[str]

@dataclass
class Media:
    id: Optional[int]
    title: Optional[Title]
    coverImage: Optional[Img]
    bannerImage: Optional[Img]
    description: Optional[str]
    format: Optional[str]
    status: Optional[str]
    averageScore: Optional[int]
    meanScore: Optional[int]
    genres: Optional[list[str]]
    synonyms: Optional[list[str]]
    popularity: Optional[int]
    trending: Optional[int]
    tags: Optional[list[str]]
    isAdult: Optional[bool]
    hashtag: Optional[str]
    trailer: Optional[str]
    characters: Optional[list[str]]
    staff: Optional[list[str]]
    relations: Optional[list[str]]
    trends: Optional[list[str]]
    reviews: Optional[list[str]]
    recommendations: Optional[list[str]]
    stats: Optional[list[str]]
    modNotes: Optional[list[str]]