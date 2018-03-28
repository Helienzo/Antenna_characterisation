from src import *

class config():
    def __init__(self,pos,dsp,rec):
        self._pos = pos
        self._dsp = dsp
        self._rec = rec


    def fileCheck(self,filename):
        return os.path.exists(str(filename))

    def save(self,filename):

        myfile = open(str(filename), "w")
        myfile.write("This is the setup file. Change the third column and be\n careful not to remove the space.\n")
        myfile.write("\n")
        myfile.write("centerFrequency = " + str((0.5e6+self._dsp.get_c_freq())/double(1e6))+"\n")
        myfile.write("lock = " + str(self._dsp.getLockMode())+"\n")
        myfile.write("delay = " + str(self._dsp.getDelay())+"\n")
        myfile.write("loopNr = " + str(self._dsp.getLoop())+"\n")
        myfile.write("loopMode = " + str(self._dsp.getLoopMode())+"\n")
        myfile.write("vecmode = " + str(self._rec.getVecMode())+"\n")
        myfile.write("R = "+ str(self._pos.getR())+"\n")
        myfile.write("sOrigin = " + str(self._pos.getSorigin())+"\n")
        myfile.write("cOrigin = " + str(self._pos.getCorigin())+"\n")
        myfile.write("xO = " + str(self._pos.getXo())+"\n")
        myfile.write("yO = " + str(self._pos.getYo())+"\n")
        myfile.write("zO = " + str(self._pos.getZo())+"\n")
        myfile.write("tMat = "+ str(self._pos.getTmat())+"\n")
        myfile.write("oPressure = " + str(self._pos.getOpressure())+"\n")
        myfile.write("oTemp = " + str(self._pos.getOtemp())+"\n")
        myfile.write("decimation = " + str(self._dsp.getDecimation())+"\n")
        myfile.write("cutoff = " + str(self._dsp.getCutoff())+"\n")
        myfile.write("transition = " + str(self._dsp.getTransition())+"\n")
        myfile.close()

    def load(self,filename):
        if os.path.exists(str(filename)):
            myfile = open(str(filename), "r")
            lineNo = 0
            for line in myfile:
                fileVec = line.split(" = ")
                lineNo += 1
                if fileVec[0] == "centerFrequency":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setCenterFreq(val)

                elif fileVec[0] == "lock":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setLock(bool(val))

                elif fileVec[0] == "delay":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setDelay(val)

                elif fileVec[0] == "loopNr":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setLoop(val)

                elif fileVec[0] == "loopMode":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    if bool(val):
                        self.setLoopAuto()

                elif fileVec[0] == "vecmode":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.vectorSaveMode(val)

                elif fileVec[0] == "R":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setR(val)

                elif fileVec[0] == "sOrigin":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setSorigin(val)

                elif fileVec[0] == "cOrigin":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setCorigin(val)

                elif fileVec[0] == "xO":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setX(val)

                elif fileVec[0] == "yO":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setY(val)

                elif fileVec[0] == "zO":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setZ(val)

                elif fileVec[0] == "tMat":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setTmat(val)

                elif fileVec[0] == "oPressure":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setOpressure(val)

                elif fileVec[0] == "oTemp":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setOtemp(val)

                elif fileVec[0] == "decimation":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setDecimation(val)

                elif fileVec[0] == "cutoff":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setCutOff(val)

                elif fileVec[0] == "transition":
                    fileVec = fileVec[1].split("\n")
                    val = ast.literal_eval(fileVec[0])
                    self.setTransition(val)

            #self.loadOrigin()

    def setLock(self,mode):
        if mode:
            self._dsp.lock()
        else:
            self._dsp.unlock()

    def setDelay(self,delTime):
        self._dsp.delay(delTime)

    def setLoop(self,loop):
        self._dsp.set_loop(loop)

    def setLoopAuto(self):
        self._dsp.set_auto_loop(1)

    def vectorSaveMode(self,mode):
        if mode:
            self._rec.vecsave()
        else:
            self._rec.vecnosave()

    def setR(self,val):
        self._pos.setR(val)

    def setSorigin(self,val):
        self._pos.setSorigin(val)

    def setCorigin(self,val):
        self._pos.setCorigin(val)

    def setX(self,val):
        self._pos.setXo(val)

    def setY(self,val):
        self._pos.setYo(val)

    def setZ(self,val):
        self._pos.setZo(val)

    def setTmat(self,val):
        self._pos.setTmat(val)

    def setOpressure(self,val):
        self._pos.setOpressure(val)

    def setOtemp(self,val):
        self._pos.setOtemp(val)

    def setOrigin(self):
        self._pos.set_origin()

    def setCenterFreq(self,centerfreq):
        self._dsp.set_c_freq(double(centerfreq)*1e6-0.5e6)

    def setDecimation(self,decimation):
        self._dsp.setDecimation(decimation)

    def setCutOff(self,cutoff):
        self._dsp.setCutoff(cutoff)

    def setTransition(self,transition):
        self._dsp.setTransition(transition)


