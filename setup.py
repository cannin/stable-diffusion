from setuptools import setup, find_packages

setup(
    name='latent-diffusion',
    version='0.0.1-mps',
    description='',
    packages=['ldm', 'ldm.models', 'ldm.models.diffusion', 'ldm.modules', 'ldm.modules.diffusionmodules', 'ldm.modules.distributions', 'ldm.modules.encoders', 'ldm.modules.image_degradation', 'ldm.modules.losses'],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)