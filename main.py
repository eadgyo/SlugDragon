from GamesFiles.Game import Game
from Maths.Point2D import Point2D
from platform import platform

def main() :
    
    game = Game()
    while game.running :       
        while game.paused :
            game.display.showMenu()
            game.input.updateMenu()
            game.input.commands_menu(game.input.player_commands_menu(game.display), game)
                
        if game.running :
            game.input.update()
            game.input.entityAction(game, game.player, game.input.player_commands())
            game.display.update(game)
            game.player.update(game.dt)
                
            for platform in game.platforms :
                game.player.manageCollision(platform)
            """for enemy in game.enemies :
                game.player.manageCollision(enemy)"""
            game.player.aim(Point2D(game.input.mouse[1][0], game.input.mouse[1][1]), game.display.window_position)
            game.player.updateRectangle()

            for enemy in game.enemies :
                pass

            for bullet in game.bullets :
                bullet.update(game.dt)
                bullet.image.setPosition(bullet.image.p2DCenter)
            #for bullet in game.bullets :
            #    bullet.image.collision(game.player.image)
            for bullet in game.bullets : 
                deleted = False
                for enemy in game.enemies :
                    if not deleted and bullet.image.collision(enemy.image) :
                        game.delBullet(bullet)
                        deleted = True
            """
            for bullet in game.bullets :
                deleted = False
                for platform in game.platforms :
                    if not deleted and bullet.image.collision(platform.image) :
                        platform.image.display(game.display.window, -game.display.window_position)
                        game.delBullet(bullet)
                        deleted = True
            """
            for bullet in game.bullets :
                deleted = False  
                for target in game.targets :
                    target.update(game.dt)
                    if not deleted and bullet.image.collision(target.image) :
                        target.image.drawRectangle(game.display.window, -game.display.window_position)
                        game.delBullet(bullet)
                        game.delTarget(target)
                        deleted = True
            for bullet in game.bullets :
                if bullet.image.p2DCenter.x < -50 or bullet.image.p2DCenter.x > game.display.window_position.x + game.display.width +50 :
                    game.delBullet(bullet)
            for bullet in game.bullets :
                if bullet.image.p2DCenter.y > 720 or bullet.image.p2DCenter.y < -50 :
                    game.delBullet(bullet)

            game.display.updatePosition(game.player)
            #game.jumpSound.play()
            game.updateTime()
                
            if len(game.targets) == 0 :
                game.pauseGame()
                game.winGame()
                
if __name__ == "__main__" :
    main()