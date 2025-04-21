from setuptools import setup

setup(


    name="Calculadora chachi",
    version="1.0",
    description="Calculadora y modulos para crear una calculadora",
    author="Jacinto Conesa",
    author_email="jacintoconesa@hotmail.com",
    url="www.pildorasinformaticas.es",
    packages=["pildoras-.Botonera_Calculadora", "pildoras-.Operaciones_Calculadora", "pildoras-.resultado_botones"],
    install_requires=[
        "tkinter",
        "re"
    ],






)