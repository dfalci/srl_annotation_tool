# -*- coding: utf-8; -*-

from threading import Thread
from flask import Flask, render_template, session, request, send_from_directory
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect, Namespace
from flask_cors import CORS
import datetime
import time
from utils.singleton import Singleton
from sent_db import SentenceDatabase
import json

@Singleton
class ServerController(object):
    """
    Controla a comunicacao com os sistemas
    """

    def __init__(self):
        async_mode = 'threading'

        self.app = Flask(__name__)
        CORS(self.app)
        self.app.config['SECRET_KEY'] = '1238-48217471-2'
        self.app.config['TEMPLATES_AUTO_RELOAD'] = True
        self.socketio = SocketIO(self.app, async_mode=async_mode)
        self.namespace = '/anotacao'


        # inicializando os binds da plataforma
        self.__bind_flask()
        self.__bind_socketio()

        self.__start_reading()


    def execute(self):
        def __run_execute():
            return self.socketio.run(self.app, '0.0.0.0', 9000)

        t = Thread(target=__run_execute)
        t.start()
        return t

    def __start_reading(self):
        def captureMessageQueue():
            while True:
                try:
                    time.sleep(1000)
                    #print 'pesquisando novos itens na fila'
                    #m = ChatQueueManager.Instance().queue.get()
                    #self.socketio.emit('machine_message', m['data'], room=m['login'], namespace=self.namespace)



                except Exception as ex:
                    print ex
                #ChatQueueManager.Instance().queue.task_done()


        self.socketio.start_background_task(captureMessageQueue)

    def __bind_socketio(self):
        self.socketio.on_event('connect', self.on_connect, namespace=self.namespace)
        self.socketio.on_event('disconnect', self.on_disconnect, namespace=self.namespace)

        self.socketio.on_event('join', self.on_join, namespace=self.namespace)
        self.socketio.on_event('tag_message', self.on_tag_message, namespace=self.namespace)

    def on_connect(self):
        session['connection_time'] = datetime.datetime.now()

    def on_disconnect(self):
        print session['connection_time']
        session['usuario'].set_logado(False)
        print 'desconectou'

    def on_join(self, message):
        """
        Registra a entrada de um cliente
        :param message:
        :return:
        """
        join_room('1')

        session['join_time'] = datetime.datetime.now() # horario em que o join foi efetuado
        session['indice'] = 0
        m = SentenceDatabase.Instance().get_question(session['indice'])
        m = m.toDict()
        self.socketio.emit('new_sentence', m, room='1', namespace=self.namespace)


    def on_tag_message(self, message):
        #ConversationResolver.Instance().user_converse(usuario, message['data'])
        print message


    def __bind_flask(self):
        self.app.add_url_rule('/anotacao', 'index', self.__show_index)
        self.app.add_url_rule('/<path:path>', 'dist', self.__send_path)

    def __send_path(self, path):
        return send_from_directory(self.app.static_folder, path)

    def __show_index(self):
        return render_template('index.html', async_mode=self.socketio.async_mode)

if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    from utils import SystemConfig
    SystemConfig.Instance().map()

    SentenceDatabase.Instance().prepare()


    c = ServerController.Instance()
    t = c.execute()
    t.join()





