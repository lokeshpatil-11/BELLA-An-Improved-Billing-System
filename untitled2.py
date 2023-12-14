ipadd=int(input()) #138101114250
masking_bit=int(input())

h= 32-masking_bit

no_subnet=2**masking_bit

no_host=2**h-2

ipadd=str(ipadd)

a=bin(int(ipadd[:3]))
b=bin(int(ipadd[3:6]))
c=bin(int(ipadd[6:9]))
d=bin(int(ipadd[9:]))

print('binary conversion of IP: ',a[2:],b[2:],c[2:],d[2:])
bin_ip=a[2:]+b[2:]+c[2:]+d[2:]
# making last h bits zero for starting address
d=d[:-h]+'0'*h
print('binary conversion of IP: ',a[2:],b[2:],c[2:],d[2:])


print('starting address: ',int(a[2:],2),int(b[2:],2),int(c[2:],2),int(d[2:],2))


# making last h bits one for ending address
d=d[:-h]+'1'*h
print('binary conversion of IP: ',a[2:],b[2:],c[2:],d[2:])


print('ending address: ',int(a[2:],2),int(b[2:],2),int(c[2:],2),int(d[2:],2))


x='1'*masking_bit+bin_ip[masking_bit:]
