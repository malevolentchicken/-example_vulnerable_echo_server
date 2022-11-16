// Vulnerable echo server
// Compile with "C:\Program Files\CodeBlocks\MinGW\bin\g++.exe" C:\Users\researcher\Desktop\vuln_echo_server.c -o C:\Users\researcher\Desktop\test.exe -lws2_32


#define _WIN32_WINNT 0x501
#undef UNICODE
#define WIN32_LEAN_AND_MEAN

#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <stdlib.h>
#include <stdio.h>

// Need to link with Ws2_32.lib
#pragma comment (lib, "Ws2_32.lib")

#define DEFAULT_BUFLEN 2048
#define DEFAULT_PORT "69"

// Misleading junk.
int important(){ 

    asm ("jmp %esp;"
         );

int i, n, t1 = 0, t2 = 1, nextTerm;

    printf("Enter the number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");

    for (i = 1; i <= n; ++i)
    {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return 0;
}

void execCMD(char *recvBuff){ // Purposely copy larger buffer over onto smaller to create a stack overflow.
    printf("--------------------------------------------------------------------------------- Command Issued recvbuffer - %i\n", sizeof(&recvBuff));
    char cmdArray[128] = {0};
    strcpy(cmdArray,  recvBuff);
}


int __cdecl main(void)
{
   
   HMODULE libHandle;

    // Loaded to give a JMP ESP
    if ((libHandle = LoadLibrary(TEXT("cygwin1.dll"))) == NULL)
    {
        printf("load failed\n");
        return 1;
    }
    if (GetProcAddress(libHandle, "send") == NULL)
    {
        printf("GetProcAddress failed\n");
        printf("%d\n", GetLastError());
        return 1;
    }
    
     
    WSADATA wsaData;
    int iResult;

    SOCKET ListenSocket = INVALID_SOCKET;
    SOCKET ClientSocket = INVALID_SOCKET;

    struct addrinfo *result = NULL;
    struct addrinfo hints;

    int iSendResult;
    char recvbuf[DEFAULT_BUFLEN] = {0};
    int recvbuflen = DEFAULT_BUFLEN;

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed with error: %d\n", iResult);
        return 1;
    }

    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    hints.ai_flags = AI_PASSIVE;

    // Resolve the server address and port
    iResult = getaddrinfo(NULL, DEFAULT_PORT, &hints, &result);
    if ( iResult != 0 ) {
        printf("getaddrinfo failed with error: %d\n", iResult);
        WSACleanup();
        return 1;
    }

    // Create a SOCKET for connecting to server
    ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    if (ListenSocket == INVALID_SOCKET) {
        printf("socket failed with error: %ld\n", WSAGetLastError());
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }

    // Setup the TCP listening socket
    iResult = bind( ListenSocket, result->ai_addr, (int)result->ai_addrlen);
    if (iResult == SOCKET_ERROR) {
        printf("bind failed with error: %d\n", WSAGetLastError());
        freeaddrinfo(result);
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    freeaddrinfo(result);

    iResult = listen(ListenSocket, SOMAXCONN);
    if (iResult == SOCKET_ERROR) {
        printf("listen failed with error: %d\n", WSAGetLastError());
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    char welcome[100] = "Ready for action.\nSend me the cmd:";
    while(1){
    // Accept a client socket
    ClientSocket = accept(ListenSocket, NULL, NULL);
    send(ClientSocket, welcome, sizeof(welcome), 0);
    
    if (ClientSocket == INVALID_SOCKET) {
        printf("accept failed with error: %d\n", WSAGetLastError());
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    // No longer need server socket
    //closesocket(ListenSocket);

    // Receive until the peer shuts down the connection
    do {

        iResult = recv(ClientSocket, recvbuf, recvbuflen, 0);
        if (iResult > 0) {
            printf("Bytes received: %d\n", iResult);
            
            char temp[sizeof(recvbuf)] = {0};
            char tmpChar[3] = {0} ;
            strncpy(tmpChar, recvbuf, 3);
            tmpChar[3] = '\0';

            if (strcmp(tmpChar, "cmd") == 0){                
                execCMD(recvbuf); // Trigger the overflow
            }

            sprintf(temp,"You sent %d bytes. - %s",iResult, recvbuf);        
            // sprintf(temp,"You sent %d bytes.",iResult); 
            iSendResult = send(ClientSocket,temp,sizeof(temp),0);

            // Echo the buffer back to the sender
            // iSendResult = send( ClientSocket, recvbuf, iResult, 0 );
            if (iSendResult == SOCKET_ERROR) {
                printf("send failed with error: %d\n", WSAGetLastError());
                closesocket(ClientSocket);
                WSACleanup();
                return 1;
            }
            printf("Bytes sent: %d\n", iSendResult);
        }
        else if (iResult == 0)
            printf("Connection closing...\n");
        else  {
            printf("recv failed with error: %d\n", WSAGetLastError());
            closesocket(ClientSocket);
            WSACleanup();
            return 1;
        }

    } while (iResult > 0); //

    }

    // shutdown the connection since we're done
    iResult = shutdown(ClientSocket, SD_SEND);
    if (iResult == SOCKET_ERROR) {
        printf("shutdown failed with error: %d\n", WSAGetLastError());
        closesocket(ClientSocket);
        WSACleanup();
        return 1;
    }

    // cleanup
    closesocket(ClientSocket);
    WSACleanup();

    return 0;
}
