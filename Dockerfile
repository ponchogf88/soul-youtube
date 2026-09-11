FROM ubuntu:24.04

LABEL maintainer="@ponchogf88"
LABEL description="AMDA Agentic Engine - 24/7 Continuous FFmpeg Stream Container"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    ca-certificates \
    curl \
    bash \
    procps \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash stream && \
    mkdir -p /home/stream/media /var/log/livestream && \
    chown -R stream:stream /home/stream /var/log/livestream

WORKDIR /home/stream

COPY --chmod=755 scripts/stream_loop.sh /home/stream/stream_loop.sh

USER stream

ENTRYPOINT ["/home/stream/stream_loop.sh"]
