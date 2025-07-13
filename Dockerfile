FROM openjdk:21
ADD target/demo-0.0.1-SNAPSHOT.jar user-mysql.jar
EXPOSE 1111
ENTRYPOINT ["java", "-jar", "user-mysql.jar"]
