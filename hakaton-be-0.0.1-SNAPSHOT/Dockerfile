FROM eclipse-temurin:25.0.1_8-jdk-ubi10-minimal

WORKDIR /app

COPY hakaton-be-0.0.1-SNAPSHOT.jar /app/hakaton-be-0.0.1-SNAPSHOT.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "hakaton-be-0.0.1-SNAPSHOT.jar"]
