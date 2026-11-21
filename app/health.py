from dataclasses import dataclass


@dataclass(frozen=True)
class HealthStatus:
    status: str = "ok"
    service: str = "pricing"

    def as_dict(self) -> dict[str, str]:
        return {"status": self.status, "service": self.service}
