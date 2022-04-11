"""
The first step is to import libraries required for developing your module. This 
example shows the creation of an abstract class which cannot be created using the 
default python libraries. Hence, the abc module needs to be imported. This module 
contains the methods typically required for creating an abstract class. Test

"""
from abc import ABC, abstractmethod


class AbstractClassTemplate(ABC):
    """
    This docstring is used to provide a brief description of the abstract class template
    and can be accessed by the users by using the 'help' function. Instances cannot be 
    created directly from an abstract class, but from child classes of the abstract class.
    """

    type = "Abstract Class"
    """
    In this example, 'type' is a class variable common to all child classes of this 
    abstract class.
    """

    def __init__(self, arg1, arg2):
        """
        The __init__ method is called every time an object is created from a class. It lets 
        the class initialize the object's attributes and serves no other purpose. 
        
        Constructs all necessary attributes for the AbstractClassTemplate object. 

        Parameters
        ----------
            arg1: float
                Provide a brief description of arg1
            arg2: float
                Provide a bried description of arg2
        """
        self._arg1 = arg1
        self._arg2 = arg2

    """
    The property decorator is a convenient way of setting, getting (and deleting) the 
    value of the variable associated with the method (in the following example, arg1 
    is the method and self._arg1 is the variable associated with the method). Using the
    @property decorator sets the getter method. Seprate decorators need to be used for 
    activating the setter and delete methods as shown in the concreteclass template.
    """

    @property
    def arg1(self):
        """Get arg1 rating of the ESS in MW"""
        return self._arg1

    """
    Getter method for arg2
    """

    @property
    def arg2(self):
        """Get energy rating of the ESS in MWh"""
        return self._arg2

    """
    The following examples illustrate the use of the @abstractmethod decorator. In an 
    abstract class, whenever we use the @abstractmethod decorator before a method, it implies 
    that we have to create the method in the child class. For instance, we must create the 
    methods _method1() and _method2() in all child classes created from this abstract class. 
    """

    @abstractmethod
    def _absmethod1(self):
        """An example of abstract method."""
        pass

    @abstractmethod
    def _absmethod2(self):
        """Another example of abstract method."""
        pass

    """
    The following are examples of concrete methods within the abstract class. These methods
    will not be preceded by the @abstractmethod decorator. Unlike abstract methods, we do 
    not need to define these methods explicitly in the child class. These methods will be 
    automatically inherited by the child class. 
    """

    def _concrmethod1(self, *args, **kwargs):
        """An example of concrete method. Using \*args and \*\*kwargs lets us pass an unspecified
        number of arguments and keyword arguments to a function, so when writing the function 
        definition, we do not need to know how many arguments will be passed to our function.
        """
        pass

    def _concrmethod2(self, *args, **kwargs):
        """Another example of concrete method."""
        pass
