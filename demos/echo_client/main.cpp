// Example echo client
#include <chrono>
#include <memory>
#include <string>
#include <thread>
#include <hv/WebSocketClient.h>

int main(int argc, char* argv[]) {
    std::string address = "ws://localhost:1145";
    auto ws_client {std::make_unique<hv::WebSocketClient>()};

    ws_client->onmessage = [](const std::string& msg) {
        std::cout << "Received message from server: ";
        std::cout << msg << "\n";
    };

    ws_client->open(address.data());
    ws_client->start();
    
    for (int i = 0; i < 5; ++i) { // Send five messages
        std::string msg;
        std::cout << "Please input message: ";
        std::cin >> msg;
        ws_client->send(msg);

        std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Wait for reply...
    }
    
    ws_client->close();
    return 0;
}
