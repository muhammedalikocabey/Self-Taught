FROM mcr.microsoft.com/java/jdk:8-zulu-alpine AS java_derleyici
COPY /source /usr/src/uygulama
WORKDIR /usr/src/uygulama
RUN javac uygulama.java


FROM mcr.microsoft.com/java/jre:8-zulu-alpine
WORKDIR /uygulama
COPY --from=java_derleyici /usr/src/uygulama .
CMD ["java", "uygulama"]
