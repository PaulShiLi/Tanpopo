from dataclasses import dataclass

DEFAULT = False

@dataclass
class PageQuery:
    total: bool
    currentPage: bool
    lastPage: bool
    hasNextPage: bool
    perPage: bool
    
    # Set the DEFAULT values for the PageQuery
    def __post_init__(self):
        self.total = self.total if self.total else DEFAULT
        self.currentPage = self.currentPage if self.currentPage else DEFAULT
        self.lastPage = self.lastPage if self.lastPage else DEFAULT
        self.hasNextPage = self.hasNextPage if self.hasNextPage else DEFAULT
        self.perPage = self.perPage if self.perPage else DEFAULT

######################
# Media Query Types #

@dataclass
class Title:
    romaji: bool
    english: bool
    native: bool
    
    def __post_init__(self):
        self.romaji = self.romaji if self.romaji else DEFAULT
        self.english = self.english if self.english else DEFAULT
        self.native = self.native if self.native else DEFAULT

@dataclass
class Date:
    year: bool
    month: bool
    day: bool
    
    def __post_init__(self):
        self.year = self.year if self.year else DEFAULT
        self.month = self.month if self.month else DEFAULT
        self.day = self.day if self.day else DEFAULT

@dataclass
class Dates:
    startDate: Date | bool
    endDate: Date | bool
    
    def __post_init__(self):
        self.startDate = self.startDate if self.startDate else DEFAULT
        self.endDate = self.endDate if self.endDate else DEFAULT

@dataclass
class Img:
    large: bool
    medium: bool
    
    def __post_init__(self):
        self.large = self.large if self.large else DEFAULT
        self.medium = self.medium if self.medium else DEFAULT

@dataclass
class MediaQuery:
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
    
    # Set the DEFAULT values for the MediaQuery
    def __post_init__(self):
        self.id = self.id if self.id else DEFAULT
        self.title = self.title if self.title else DEFAULT
        self.coverImage = self.coverImage if self.coverImage else DEFAULT
        self.bannerImage = self.bannerImage if self.bannerImage else DEFAULT
        self.description = self.description if self.description else DEFAULT
        self.format = self.format if self.format else DEFAULT
        self.status = self.status if self.status else DEFAULT
        self.averageScore = self.averageScore if self.averageScore else DEFAULT
        self.meanScore = self.meanScore if self.meanScore else DEFAULT
        self.genres = self.genres if self.genres else DEFAULT
        self.synonyms = self.synonyms if self.synonyms else DEFAULT
        self.popularity = self.popularity if self.popularity else DEFAULT
        self.trending = self.trending if self.trending else DEFAULT
        self.tags = self.tags if self.tags else DEFAULT
        self.isAdult = self.isAdult if self.isAdult else DEFAULT
        self.hashtag = self.hashtag if self.hashtag else DEFAULT
        self.trailer = self.trailer if self.trailer else DEFAULT
        self.characters = self.characters if self.characters else DEFAULT
        self.staff = self.staff if self.staff else DEFAULT
        self.trends = self.trends if self.trends else DEFAULT
        self.reviews = self.reviews if self.reviews else DEFAULT
        self.recommendations = self.recommendations if self.recommendations else DEFAULT
        self.stats = self.stats if self.stats else DEFAULT
        self.modNotes = self.modNotes if self.modNotes else DEFAULT
        self.isRecommendationBlocked = self.isRecommendationBlocked if self.isRecommendationBlocked else DEFAULT
        self.airingSchedule = self.airingSchedule if self.airingSchedule else DEFAULT
        self.rankings = self.rankings if self.rankings else DEFAULT
        self.mediaListEntry = self.mediaListEntry if self.mediaListEntry else DEFAULT
        self.externalLinks = self.externalLinks if self.externalLinks else DEFAULT
        self.siteUrl = self.siteUrl if self.siteUrl else DEFAULT
        self.autoCreateForumThread = self.autoCreateForumThread if self.autoCreateForumThread else DEFAULT
        self.relations = self.relations if self.relations else DEFAULT

######################
# Anime Query Types #

@dataclass
class AiringSchedule:
    airingAt: bool
    timeUntilAiring: bool
    episode: bool
    
    def __post_init__(self):
        self.airingAt = self.airingAt if self.airingAt else DEFAULT
        self.timeUntilAiring = self.timeUntilAiring if self.timeUntilAiring else DEFAULT
        self.episode = self.episode if self.episode else DEFAULT

@dataclass
class AnimeQuery(MediaQuery):
    airingSchedule: AiringSchedule
    rankings: bool
    mediaListEntry: bool
    externalLinks: bool
    siteUrl: bool
    autoCreateForumThread: bool
    
    def __post_init__(self):
        super().__post_init__()
        self.airingSchedule = self.airingSchedule if self.airingSchedule else DEFAULT
        self.rankings = self.rankings if self.rankings else DEFAULT
        self.mediaListEntry = self.mediaListEntry if self.mediaListEntry else DEFAULT
        self.externalLinks = self.externalLinks if self.externalLinks else DEFAULT
        self.siteUrl = self.siteUrl if self.siteUrl else DEFAULT
        self.autoCreateForumThread = self.autoCreateForumThread if self.autoCreateForumThread else DEFAULT

######################
# Manga Query Types #
@dataclass
class MangaQuery(MediaQuery):
    chapters: bool
    volumes: bool
    isHentai: bool
    publicationDemographic: bool
    
    def __post_init__(self):
        super().__post_init__()
        self.chapters = self.chapters if self.chapters else DEFAULT
        self.volumes = self.volumes if self.volumes else DEFAULT
        self.isHentai = self.isHentai if self.isHentai else DEFAULT
        self.publicationDemographic = self.publicationDemographic if self.publicationDemographic else DEFAULT