#include <boost/asio.hpp>
#include <iostream>
#include <iomanip>
#include <chrono>
#include <boost/regex.hpp>
#include <atomic>

using namespace boost::asio;
using ip::tcp;
using std::string;
using std::cout;
using std::endl;

std::atomic<bool> run = true;

io_service service;

//listen for new conn
tcp::acceptor acceptor_(service, tcp::endpoint(tcp::v4(), 25566));

void recurssive_new_connection()
{


	//socket creation
	tcp::socket sock(service);

	//waiting for the connection
	acceptor_.accept(sock);

	std::thread(recurssive_new_connection).detach();

	while (true)
	{
		boost::system::error_code ec;

		//read(string)
		streambuf buf;
		read_until(sock, buf, "\n", ec);
		if (ec) break;

		string data = boost::asio::buffer_cast<const char*>(buf.data());

		std::cout << "[Server]: recieved data:" << std::quoted(data) << std::endl;

		//write
		write(sock, boost::asio::buffer("[Echo]: your data:" + data), ec);
		if (ec) std::cerr << "[Write Err]: " << boost::system::system_error(ec).what() << std::endl;
	}

	while (run)
	{
		using namespace std::literals::chrono_literals;
		std::this_thread::sleep_for(1ms);
	}
}

int main()
{
	recurssive_new_connection();
}