from datetime import datetime
class viaje():
	def __init__(self,Colectivo,horario,monto):
		self.empresa=colectivo.empresa
		self.linea=colectivo.linea
		self.numero_de_interno=colectivo.numero_de_interno
		self.horario=datetime.strptime(horario,"%d/%m/%Y %H:%M")
		self.monto=monto


class Colectivo:
	def __init__(self, empresa, linea, numero_de_interno):
		self.empresa = empresa
		self.linea = linea
		self.numero_de_interno = numero_de_interno
	

class Tarjeta:
		self.trasbordo = 0
		for i in range (0,10):
			self.Viaje[i].colectivo = self.Viaje[].colectivo 	
			self.Viaje[i].horario = self.Viaje[].horario
			self.Viaje[i].monto = self.Viaje[].monto
		

	def recarga(self,monto):
		self.saldo = self.saldo + monto
		if monto > 196:
			if monto > 367:
				self.saldo =self.saldo + 92
			else:
				self.saldo =self.saldo + 34

	def saldo(self):
		print ("Su saldo es {}").format(self.saldo)
	def viajesrealizados(self):
		
 		for i in range (0,10):
 			print self.Viaje[i].colectivo
 			print self.Viaje[i].horario
 			print self.Viaje[i].monto


class TarjetaComun (Tarjeta):
	def __init__(self,saldo):
		self.saldo = saldo
	def pagarboleto(self,cole,horarioI):
		horario = datetime.strptime(horarioI,"%d/%m/%Y %H:%M")
		diferencia=(horario - self.viaje[0].horario)
			if (Colectivo.numero_de_interno != cole.numero_de_interno and diferencia.seconds <= 3600 and self.transbordo ==0):
				if (self.saldo > 1.90):
				for i in range (0,10):
					self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
					self.Viaje[10-i].horario = self.Viaje[9-i].horario
					self.Viaje[10-i].monto = self.Viaje[9-i].monto
					self.saldo = self.saldo - 1.90
					self.Viaje[0].colectivo = cole
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 1.90
					self.transbordo=self.transbordo+1
					return true
				else:
					print bobo sin credito
					return false
			else:
				if (self.saldo > 5.75):
				for i in range (0,10):
					self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
					self.Viaje[10-i].horario = self.Viaje[9-i].horario
					self.Viaje[10-i].monto = self.Viaje[9-i].monto
					self.saldo = self.saldo - 5.75
					self.Viaje[0].colectivo = cole
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 5.75
					self.transbordo=0
					return true
				else:
					print("bobo sin redito")
					return false




class TarjetaMedioBoleto (Tarjeta):
	def __init__(self,saldo):
		self.saldo = saldo
	def pagarboleto(self,Colectivo,(fecha)):
		horario = datetime.strptime(horarioI,"%d/%m/%Y %H:%M")
		ahora = datetime.strptime(date.now(), "%H:%M")
		diferencia=(horario - self.viaje[0].horario)
		if(ahora.hours<=6 and ahora.hours>=0)	
			diferencia=(horario - self.viaje[0].horario)
				if (Colectivo.numero_de_interno != cole.numero_de_interno and diferencia.seconds <= 3600 and self.transbordo ==0):
					if (self.saldo > 0.96):
					for i in range (0,10):
						self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
						self.Viaje[10-i].horario = self.Viaje[9-i].horario
						self.Viaje[10-i].monto = self.Viaje[9-i].monto
						self.saldo = self.saldo - 0.96
						self.Viaje[0].colectivo = cole
						self.Viaje[0].horario = horario
						self.Viaje[0].monto = 0.96
						self.transbordo=self.transbordo+1
						return true
					else:
						print bobo sin credito
						return false
				else:
					if (self.saldo > 2.90):
					for i in range (0,10):
						self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
						self.Viaje[10-i].horario = self.Viaje[9-i].horario
						self.Viaje[10-i].monto = self.Viaje[9-i].monto
						self.saldo = self.saldo - 2.90
						self.Viaje[0].colectivo = cole
						self.Viaje[0].horario = horario
						self.Viaje[0].monto = 2.90
						self.transbordo=0
						return true
					else:
						print("bobo sin redito")
						return false
		else:
			if (Colectivo.numero_de_interno != cole.numero_de_interno and diferencia.seconds <= 3600 and self.transbordo ==0):
				if (self.saldo > 1.90):
				for i in range (0,10):
					self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
					self.Viaje[10-i].horario = self.Viaje[9-i].horario
					self.Viaje[10-i].monto = self.Viaje[9-i].monto
					self.saldo = self.saldo - 1.90
					self.Viaje[0].colectivo = cole
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 1.90
					self.transbordo=self.transbordo+1
					return true
				else:
					print bobo sin credito
					return false
			else:
				if (self.saldo > 5.75):
				for i in range (0,10):
					self.Viaje[10-i].colectivo = self.Viaje[9-i].colectivo 	
					self.Viaje[10-i].horario = self.Viaje[9-i].horario
					self.Viaje[10-i].monto = self.Viaje[9-i].monto
					self.saldo = self.saldo - 5.75
					self.Viaje[0].colectivo = cole
					self.Viaje[0].horario = horario
					self.Viaje[0].monto = 5.75
					self.transbordo=0
					return true
				else:
					print("bobo sin redito")
					return false
					
					
					#imbecil
