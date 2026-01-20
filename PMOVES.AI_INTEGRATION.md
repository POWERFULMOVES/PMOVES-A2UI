# PMOVES.AI Integration Guide for PMOVES A2UI

## Integration Complete

The PMOVES.AI integration template has been applied to PMOVES A2UI.

## Next Steps

### 1. Customize Environment Variables

Edit the following files with your service-specific values:

- `env.shared` - Base environment configuration
- `env.tier-ui` - UI tier specific configuration
- `chit/secrets_manifest_v2.yaml` - Add your service's required secrets

### 2. Update Docker Compose

Add the PMOVES.AI environment anchor to your `docker-compose.yml`:

```yaml
services:
  a2ui:
    <<: [*env-tier-ui, *pmoves-healthcheck]
    # Your existing service configuration...
```

### 3. Integrate Health Check

Add the health check endpoint to your service:

```python
from pmoves_health import add_custom_check, get_health_status

@app.get("/healthz")
async def health_check():
    return await get_health_status()
```

### 4. Add Service Announcement

Add NATS service announcement to your startup:

```python
from pmoves_announcer import announce_service

@app.on_event("startup")
async def startup():
    await announce_service(
        slug="a2ui",
        name="PMOVES A2UI",
        url=f"http://a2ui:3737",
        port=3737,
        tier="ui"
    )
```

### 5. Test Integration

```bash
# Test health check
curl http://localhost:3737/healthz

# Verify environment variables loaded
docker compose exec a2ui env | grep PMOVES

# Verify NATS announcement
nats sub "services.announce.v1"
```

## Service Details

- **Name:** PMOVES A2UI
- **Slug:** a2ui
- **Tier:** ui
- **Port:** 3737
- **Health Check:** http://localhost:3737/healthz
- **NATS Enabled:** True
- **GPU Enabled:** False

## Files Created

- `env.shared` - Base PMOVES.AI environment
- `env.tier-ui` - Tier-specific environment
- `chit/secrets_manifest_v2.yaml` - CHIT secrets configuration
- `pmoves_health/` - Health check module
- `pmoves_announcer/` - NATS service announcer
- `pmoves_registry/` - Service registry client
- `docker-compose.pmoves.yml` - PMOVES.AI YAML anchors

## Support

For questions or issues, see the PMOVES.AI documentation.
