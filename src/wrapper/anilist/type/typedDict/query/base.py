from typing import TypedDict

class PageArgs(TypedDict):
    page: int
    perPage: int
    search: str

class PageQuery(TypedDict):
    total: bool
    currentPage: bool
    lastPage: bool
    hasNextPage: bool
    perPage: bool

######################
# Media Query Types #

class Title(TypedDict):
    romaji: bool
    english: bool
    native: bool

class Date(TypedDict):
    year: bool
    month: bool
    day: bool

class Dates(TypedDict):
    startDate: Date | bool
    endDate: Date | bool

class Img(TypedDict):
    large: bool
    medium: bool

class MediaQuery(TypedDict):
    id: int
    title: Title
    coverImage: Img | bool
    bannerImage: Img | bool
    description: bool
    format: bool
    status: bool
    averageScore: bool
    meanScore: bool
    genres: bool
    synonyms: bool
    popularity: bool
    trending: bool
    tags: bool
    isAdult: bool
    hashtag: bool
    trailer: bool
    characters: bool
    staff: bool
    trends: bool
    reviews: bool
    recommendations: bool
    stats: bool
    modNotes: bool
    isRecommendationBlocked: bool
    airingSchedule: bool
    rankings: bool
    mediaListEntry: bool
    externalLinks: bool
    siteUrl: bool
    autoCreateForumThread: bool
    relations: bool

######################
# Anime Query Types #
class AiringSchedule(TypedDict):
    airingAt: bool
    timeUntilAiring: bool
    episode: bool

class AnimeQuery(MediaQuery):
    episodes: bool
    duration: bool
    season: bool
    seasonYear: bool
    seasonInt: bool
    seasonYear: bool
    seasonInt: bool
    source: bool
    studios: bool
    streamingEpisodes: bool
    nextAiringEpisode: AiringSchedule | bool
    airingProgression: bool

######################
# Manga Query Types #
class MangaQuery(MediaQuery):
    chapters: bool
    volumes: bool
    isHentai: bool
    publicationDemographic: bool
