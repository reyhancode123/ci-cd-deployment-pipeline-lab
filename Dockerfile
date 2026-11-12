FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 10001 appuser
COPY --chown=appuser:appuser app/ ./app/
ENV APP_VERSION=1.0.0
EXPOSE 8000
USER appuser
CMD ["python", "-m", "app.server"]
