from pymiere.core import _format_object_to_py, _format_object_to_es, _eval_script_returning_object
from pymiere.autogenerated.premiere_objects import *


def _eval_on_global_object(extend_property):
    result = _eval_script_returning_object(extend_property)
    if result == "undefined":
        return None
    # if it's an object search if class exists and return objects creation arguments
    if isinstance(result, dict) and "isObject" in result and result["isObject"] is True:
        # create key word argument list to create the object
        kwargs = result["objectValues"]
        kwargs.update(pymiere_id=result["pymiereId"])
        return kwargs
    return result


class StartVars(object):
    def __init__(self, NaN=None, Infinity=None, undefined=None, qe=None, app=None, document=None, ProjectItemType=None, ScratchDiskType=None, RegisteredDirectories=None, UtilityFunctions=None, Dollar=None, Math=None, premierepro13=None, AEFTBridge=None, PHXSBridge=None, CCXHostBridge=None, f=None, JSON=None):
        PymiereBaseObject._check_init_args({'NaN':NaN, 'Infinity':Infinity, 'undefined':undefined, 'qe':qe, 'app':app, 'document':document, 'ProjectItemType':ProjectItemType, 'ScratchDiskType':ScratchDiskType, 'RegisteredDirectories':RegisteredDirectories, 'UtilityFunctions':UtilityFunctions, 'Dollar':Dollar, 'Math':Math, 'premierepro13':premierepro13, 'AEFTBridge':AEFTBridge, 'PHXSBridge':PHXSBridge, 'CCXHostBridge':CCXHostBridge, 'f':f, 'JSON':JSON})
        super(StartVars, self).__init__()
        self.__NaN = NaN
        self.__Infinity = Infinity
        self.__undefined = undefined
        self.__qe = qe
        self.__app = app
        self.__document = document
        self.__ProjectItemType = ProjectItemType
        self.__ScratchDiskType = ScratchDiskType
        self.__RegisteredDirectories = RegisteredDirectories
        self.__UtilityFunctions = UtilityFunctions
        self.__Dollar = Dollar
        self.__Math = Math
        self.__premierepro13 = premierepro13
        self.__AEFTBridge = AEFTBridge
        self.__PHXSBridge = PHXSBridge
        self.__CCXHostBridge = CCXHostBridge
        self.__f = f
        self.__JSON = JSON

    # ----- PROPERTIES -----
    @property
    def NaN(self):
        self.__NaN = _eval_on_global_object('NaN')
        return self.__NaN
    @NaN.setter
    def NaN(self, NaN):
        PymiereBaseObject._check_type(NaN, float, 'StartVars.NaN')
        _eval_on_global_object("NaN = {}".format(_format_object_to_es(NaN)))
        self.__NaN = NaN

    @property
    def Infinity(self):
        self.__Infinity = _eval_on_global_object('Infinity')
        return self.__Infinity
    @Infinity.setter
    def Infinity(self, Infinity):
        PymiereBaseObject._check_type(Infinity, float, 'StartVars.Infinity')
        _eval_on_global_object("Infinity = {}".format(_format_object_to_es(Infinity)))
        self.__Infinity = Infinity

    @property
    def undefined(self):
        self.__undefined = _eval_on_global_object('undefined')
        return self.__undefined
    @undefined.setter
    def undefined(self, undefined):
        PymiereBaseObject._check_type(undefined, None, 'StartVars.undefined')
        _eval_on_global_object("undefined = {}".format(_format_object_to_es(undefined)))
        self.__undefined = undefined

    @property
    def qe(self):
        self.__qe = _format_object_to_py(_eval_script_returning_object('qe'))
        return self.__qe
    @qe.setter
    def qe(self, qe):
        raise AttributeError("Attribute 'qe' is read-only")

    @property
    def app(self):
        self.__app = Application(**_eval_script_returning_object('app', as_kwargs=True))
        return self.__app
    @app.setter
    def app(self, app):
        raise AttributeError("Attribute 'app' is read-only")

    @property
    def document(self):
        self.__document = Document(**_eval_script_returning_object('document', as_kwargs=True))
        return self.__document
    @document.setter
    def document(self, document):
        raise AttributeError("Attribute 'document' is read-only")

    @property
    def ProjectItemType(self):
        self.__ProjectItemType = ProjectItemType(**_eval_script_returning_object('ProjectItemType', as_kwargs=True))
        return self.__ProjectItemType
    @ProjectItemType.setter
    def ProjectItemType(self, ProjectItemType):
        raise AttributeError("Attribute 'ProjectItemType' is read-only")

    @property
    def ScratchDiskType(self):
        self.__ScratchDiskType = ScratchDiskType(**_eval_script_returning_object('ScratchDiskType', as_kwargs=True))
        return self.__ScratchDiskType
    @ScratchDiskType.setter
    def ScratchDiskType(self, ScratchDiskType):
        raise AttributeError("Attribute 'ScratchDiskType' is read-only")

    @property
    def RegisteredDirectories(self):
        self.__RegisteredDirectories = RegisteredDirectories(**_eval_script_returning_object('RegisteredDirectories', as_kwargs=True))
        return self.__RegisteredDirectories
    @RegisteredDirectories.setter
    def RegisteredDirectories(self, RegisteredDirectories):
        raise AttributeError("Attribute 'RegisteredDirectories' is read-only")

    @property
    def UtilityFunctions(self):
        self.__UtilityFunctions = UtilityFunctions(**_eval_script_returning_object('UtilityFunctions', as_kwargs=True))
        return self.__UtilityFunctions
    @UtilityFunctions.setter
    def UtilityFunctions(self, UtilityFunctions):
        raise AttributeError("Attribute 'UtilityFunctions' is read-only")

    @property
    def Dollar(self):
        self.__Dollar = _format_object_to_py(_eval_script_returning_object('Dollar'))
        return self.__Dollar
    @Dollar.setter
    def Dollar(self, Dollar):
        raise AttributeError("Attribute 'Dollar' is read-only")

    @property
    def Math(self):
        self.__Math = Math(**_eval_script_returning_object('Math', as_kwargs=True))
        return self.__Math
    @Math.setter
    def Math(self, Math):
        raise AttributeError("Attribute 'Math' is read-only")

    @property
    def premierepro13(self):
        self.__premierepro13 = _format_object_to_py(_eval_script_returning_object('premierepro13'))
        return self.__premierepro13
    @premierepro13.setter
    def premierepro13(self, premierepro13):
        _eval_on_global_object("premierepro13 = {}".format(_format_object_to_es(premierepro13)))
        self.__premierepro13 = premierepro13

    @property
    def AEFTBridge(self):
        self.__AEFTBridge = _format_object_to_py(_eval_script_returning_object('AEFTBridge'))
        return self.__AEFTBridge
    @AEFTBridge.setter
    def AEFTBridge(self, AEFTBridge):
        _eval_on_global_object("AEFTBridge = {}".format(_format_object_to_es(AEFTBridge)))
        self.__AEFTBridge = AEFTBridge

    @property
    def PHXSBridge(self):
        self.__PHXSBridge = _format_object_to_py(_eval_script_returning_object('PHXSBridge'))
        return self.__PHXSBridge
    @PHXSBridge.setter
    def PHXSBridge(self, PHXSBridge):
        _eval_on_global_object("PHXSBridge = {}".format(_format_object_to_es(PHXSBridge)))
        self.__PHXSBridge = PHXSBridge

    @property
    def CCXHostBridge(self):
        self.__CCXHostBridge = _format_object_to_py(_eval_script_returning_object('CCXHostBridge'))
        return self.__CCXHostBridge
    @CCXHostBridge.setter
    def CCXHostBridge(self, CCXHostBridge):
        _eval_on_global_object("CCXHostBridge = {}".format(_format_object_to_es(CCXHostBridge)))
        self.__CCXHostBridge = CCXHostBridge

    @property
    def f(self):
        self.__f = File(**_eval_script_returning_object('f', as_kwargs=True))
        return self.__f
    @f.setter
    def f(self, f):
        PymiereBaseObject._check_type(f, File, 'StartVars.f')
        _eval_on_global_object("f = {}".format(_format_object_to_es(f)))
        self.__f = f

    @property
    def JSON(self):
        self.__JSON = _format_object_to_py(_eval_script_returning_object('JSON'))
        return self.__JSON
    @JSON.setter
    def JSON(self, JSON):
        _eval_on_global_object("JSON = {}".format(_format_object_to_es(JSON)))
        self.__JSON = JSON


    # ----- FUNCTIONS -----
    def encodeURI(self, text):
        """
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.encodeURI"')
        return _eval_on_global_object("encodeURI({})".format(_format_object_to_es(text)))

    def encodeURIComponent(self, text):
        """
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.encodeURIComponent"')
        return _eval_on_global_object("encodeURIComponent({})".format(_format_object_to_es(text)))

    def decodeURI(self, uri):
        """
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.decodeURI"')
        return _eval_on_global_object("decodeURI({})".format(_format_object_to_es(uri)))

    def decodeURIComponent(self, uri):
        """
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.decodeURIComponent"')
        return _eval_on_global_object("decodeURIComponent({})".format(_format_object_to_es(uri)))

    def escape(self, text):
        """
        :type text: str
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.escape"')
        return _eval_on_global_object("escape({})".format(_format_object_to_es(text)))

    def eval(self, source):
        """
        :type source: str
        """
        PymiereBaseObject._check_type(source, str, 'arg "source" of function "StartVars.eval"')
        return _eval_on_global_object("eval({})".format(_format_object_to_es(source)))

    def uneval(self, what):
        """
        :type what: any
        """
        PymiereBaseObject._check_type(what, any, 'arg "what" of function "StartVars.uneval"')
        return _eval_on_global_object("uneval({})".format(_format_object_to_es(what)))

    def isFinite(self, what):
        """
        :type what: float
        """
        PymiereBaseObject._check_type(what, float, 'arg "what" of function "StartVars.isFinite"')
        return _eval_on_global_object("isFinite({})".format(_format_object_to_es(what)))

    def isNaN(self, what):
        """
        :type what: float
        """
        PymiereBaseObject._check_type(what, float, 'arg "what" of function "StartVars.isNaN"')
        return _eval_on_global_object("isNaN({})".format(_format_object_to_es(what)))

    def parseInt(self, text, base):
        """
        :type text: str
        :type base: float
        """
        PymiereBaseObject._check_type(text, str, 'arg "text" of function "StartVars.parseInt"')
        PymiereBaseObject._check_type(base, float, 'arg "base" of function "StartVars.parseInt"')
        return _eval_on_global_object("parseInt({}, {})".format(_format_object_to_es(text), _format_object_to_es(base)))

    def parseFloat(self, txt):
        """
        :type txt: str
        """
        PymiereBaseObject._check_type(txt, str, 'arg "txt" of function "StartVars.parseFloat"')
        return _eval_on_global_object("parseFloat({})".format(_format_object_to_es(txt)))

    def unescape(self, uri):
        """
        :type uri: str
        """
        PymiereBaseObject._check_type(uri, str, 'arg "uri" of function "StartVars.unescape"')
        return _eval_on_global_object("unescape({})".format(_format_object_to_es(uri)))

    def localize(self, what):
        """
        :type what: any
        """
        PymiereBaseObject._check_type(what, any, 'arg "what" of function "StartVars.localize"')
        return _eval_on_global_object("localize({})".format(_format_object_to_es(what)))

    def isXMLName(self, name):
        """
        :type name: str
        """
        PymiereBaseObject._check_type(name, str, 'arg "name" of function "StartVars.isXMLName"')
        return _eval_on_global_object("isXMLName({})".format(_format_object_to_es(name)))

    def setDefaultXMLNamespace(self, ns):
        """
        :type ns: Namespace
        """
        return _eval_on_global_object("setDefaultXMLNamespace({})".format(_format_object_to_es(ns)))

    def alert(self, prompt):
        """
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.alert"')
        _eval_on_global_object("alert({})".format(_format_object_to_es(prompt)))

    def confirm(self, prompt):
        """
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.confirm"')
        return _eval_on_global_object("confirm({})".format(_format_object_to_es(prompt)))

    def prompt(self, prompt):
        """
        :type prompt: str
        """
        PymiereBaseObject._check_type(prompt, str, 'arg "prompt" of function "StartVars.prompt"')
        return _eval_on_global_object("prompt({})".format(_format_object_to_es(prompt)))