FROM jupyter/minimal-notebook

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y graphviz

WORKDIR /home/jovyan/work/epl-kernel/

COPY epl-kernel/ ./

RUN chown -R $NB_USER:users /home/$NB_USER/work/epl-kernel

USER jovyan

RUN pip install  -e .

RUN jupyter eplkernel install --user