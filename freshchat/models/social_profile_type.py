from enum import Enum


class SocialProfileType(str, Enum):
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"
    SKYPE = "skype"
    TWITTER = "twitter"

    def __str__(self) -> str:
        return str(self.value)
