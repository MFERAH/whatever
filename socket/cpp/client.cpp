#include <boost/asio.hpp>
#include <iostream>
#include <iomanip>

using namespace boost::asio;
using ip::tcp;
using std::string;
using std::cout;
using std::endl;

int main(int argc, char** argv)
{
	io_service service;

	//socket creation
	tcp::socket sock(service);


	//connect
	if (argc == 1)
		sock.connect(tcp::endpoint(
			ip::address::from_string("127.0.0.1"), 25566));
	else
		sock.connect(tcp::endpoint(
			ip::address::from_string(argv[1]), std::stoi(argv[2])));


	boost::system::error_code ec;
	for (int i = 0; true; i++)
	{

		//request
		/*write(sock, buffer("[Request]: " + []()
			{
				std::string str;
				for (size_t i = 0; i < 233; i++)
					str += "motherfucker asshole";
				return str;
			}() +"hello from client\n"));*/ //uncomment these line to see interesting thing
		write(sock, buffer("[Request]: hello from client for " + std::to_string(i) + " times \n"), ec);
		if (ec) std::cerr << "[Write Err]: " << boost::system::system_error(ec).what() << std::endl;


		//recive
		streambuf recv_buf;
		read_until(sock, recv_buf, "\n", ec);
		if (ec) std::cerr << "[Read Err]: " << boost::system::system_error(ec).what() << std::endl;

		try
		{
			std::string recv_data = buffer_cast<const char*>(recv_buf.data());
			std::cout << "[Client]: recieved data:" << std::quoted(recv_data) << std::endl;
		}
		catch (const boost::system::system_error& err)
		{
			std::cout << "Exception" << err.what() << std::endl;
		}
	}
	sock.shutdown(socket_base::shutdown_type::shutdown_both, ec);
	if (ec) std::cerr << "[Shutdown Err]: " << boost::system::system_error(ec).what() << std::endl;
	sock.close();
}