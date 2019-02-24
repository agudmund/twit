#!/usr/bin/env python
# *-* coding:utf-8 *-*
#
# Maya flash card generator
#    reads input from Twitter feed through an external script and displays it as workspace graphics in Maya 
#
#   -aeVar 2017

import sys
import socket    
import random

class Connect( object ):
    def __init__( self , port=47000 ):
        self.ip = socket.gethostbyname( socket.gethostname() )
        self.port = port

    def send( self , command='' ):
        """Sends a command from an external script to Maya's command port"""

        client = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
        client.connect( ( "127.0.0.1" , self.port ) )
        client.send( command )

        result = client.recv( 1024 )
        client.close()

        return result

class Create:
	def __init__(self):
		self.name = 'Flashcards'
		self.index = 0

	def create(self, letter):

		# Import the libraries
		_c.send('python("import random")')
		_c.send('python("import maya.mel")')

		# Create the plane, position it, and scale it.
		OBJ = _c.send('polyPlane()')
		_c.send('scale(0.5,1,1)')
		_c.send('python("maya.cmds.move(%s, 0, %s )")' % ( self.index, random.uniform(-0.3,0.3)) )
		
		# Create the shader
		fileNode = '%s_fileTexture' % letter
		SHD = _c.send('shadingNode -asShader -name %s lambert' % letter )
		FIL = _c.send('createNode file -name %s' % fileNode )
		print 'Created Shader: %s' % SHD
		print 'Created file Node: %s' % fileNode

		# Connect it all together
		_c.send("connectAttr %s.outColor %s.color" % ( fileNode, letter ) )
		letter_on_disk = r'"C:\\Users\\normal\\Projects\\Typing\\Unity\\Assets\\_Textures\\Alphabet\\Graham Placeholders\\%s.jpg"' % letter
		_c.send('setAttr %s.fileTextureName -type "string" %s ' % ( fileNode, letter_on_disk ) )
		_c.send('select %s' % OBJ)
		_c.send('hyperShade -assign %s' % letter)
		_c.send('select -cl')
		self.index += 0.6

		return True


if __name__ == '__main__':
	_c = Connect()
	c = Create()
	print ( _c.ip )
	print ( _c.port )
	for n in sys.argv[-1]:
		c.create(n)
