from enum import Enum


class SmtpSecurity(str, Enum):
    NONE = "none"
    SSLTLS = "sslTls"
    STARTTLS = "startTls"

    def __str__(self) -> str:
        return str(self.value)
