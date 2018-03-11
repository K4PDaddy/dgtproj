#!/usr/bin/env python3

import os,sys,time,json,socket,datetime,argparse

def args():
        parser = argparse.ArgumentParser(
                description='',
                epilog='')
        parser.add_argument('-p','--port', help= "Enter a port to listen on")
        args = parser.parse_args()
        return args

args=args()
if args.port == None:
	sys.exit("\t[!] Please specify a port with '-p'")	

def main():
	os.system('clear')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('0.0.0.0', int(args.port)))
	s.listen(10)
	while True:
		conn, addr = s.accept()
		data = conn.recv(4096)
		logging = open('log.txt', 'a')
		try:
			logging.write('\n\t[!] ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' ' + addr[0] + ':' + str(addr[1]) + ' sent:\n' + data.decode(errors='ignore').rstrip('\n')+'\n')
			print('\n\t[!] ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' ' + addr[0] + ':' + str(addr[1]) + ' sent:\n' + data.decode(errors='ignore').rstrip('\n'))
		except:
			logging.write('\n\t[!] ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' ' + addr[0] + ':' + str(addr[1]) + ' sent:\n' + hex(data).rstrip()+'\n')
			print('\n\t[!] ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ' ' + addr[0] + ':' + str(addr[1]) + ' sent:\n' + hex(data).rstrip())
		try:
			if json.loads(data.decode('utf-8').rstrip()):
				logging.write("OH, JSON? I LIKE WHAT YOU GOT, GOOOD JOB\n")
				print("OH, JSON? I LIKE WHAT YOU GOT, GOOOD JOB")
				conn.sendall(b"OH, JSON? I LIKE WHAT YOU GOT, GOOOD JOB\n")
		except:
			logging.write("NOT JSON, BOOOO, DISQUALIFIED\n")
			print("NOT JSON, BOOOO, DISQUALIFIED")
			conn.sendall(b"NOT JSON, BOOOO, DISQUALIFIED\n")
		logging.close()
		conn.close()

main()
