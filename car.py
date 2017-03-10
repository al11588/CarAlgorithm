import Algorithmia

class cars():
	"""docstring for cars"""
def caralgo():
	input = "http://o.aolcdn.com/dims-shared/dims3/GLOB/legacy_thumbnail/800x450/format/jpg/quality/85/http://o.aolcdn.com/hss/storage/midas/e0004f55e707d69677308e17ae6b9cf5/203975004/03-2012-tesla-model-s-fd-1347336750.jpg"
	client = Algorithmia.client('simbLlY25wXiSb3Ql+Zm+1NgBy41')
	algo = client.algo('LgoBE/CarMakeandModelRecognition/0.3.0')
	print (algo.pipe(input))

caralgo()
