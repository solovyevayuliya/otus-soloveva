#include <stdio.h>
#include <winsock2.h>

#define MAX_CLIENTS 10
#define BUFFER_SIZE 1024

int main() {
    WSADATA wsaData;
    SOCKET serverSocket, clientSockets[MAX_CLIENTS];
    struct sockaddr_in serverAddr, clientAddr;
    char buffer[BUFFER_SIZE];
    int clientCount = 0;
    int i;

    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        perror("WSAStartup failed");
        return 1;
    }

    if ((serverSocket = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        perror("Socket creation failed");
        return 1;
    }

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8888);

    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        perror("Socket binding failed");
        return 1;
    }

    if (listen(serverSocket, MAX_CLIENTS) == SOCKET_ERROR) {
        perror("Socket listening failed");
        return 1;
    }

    printf("Server started. Waiting for incoming connections...\n");

    while (1) {
        int addrLen = sizeof(clientAddr);
        SOCKET clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &addrLen);
        if (clientSocket == INVALID_SOCKET) {
            perror("Accept failed");
            return 1;
        }

        clientSockets[clientCount++] = clientSocket;

        printf("Client connected: %s:%d\n", inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port));

        while (1) {
            memset(buffer, 0, BUFFER_SIZE);
            int bytesRead = recv(clientSocket, buffer, BUFFER_SIZE, 0);
            if (bytesRead <= 0) {
                printf("Client disconnected: %s:%d\n", inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port));
                break;
            }

            printf("Received message from %s:%d: %s", inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port), buffer);

            for (i = 0; i < clientCount; i++) {
                if (clientSockets[i] != INVALID_SOCKET && clientSockets[i] != clientSocket) {
                    send(clientSockets[i], buffer, bytesRead, 0);
                }
            }
        }
    }
}