from flask import Flask, render_template
import game_logic as gl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def main():
    grid_size = 4
    grid = gl.new_game(grid_size)

    commands = {'w': gl.move_up, 's': gl.move_down, 'a': gl.move_left, 'd': gl.move_right, 'q': True}
    game_over = False

    while not game_over:
        gl.print_grid(grid)
        move = input("Next move. Use w (up), a (left), s (down), or d (right): ").strip().lower()

        if move in commands:
            if move == 'q':
                print ("Game aborted.")
                return                
            new_grid = commands[move](grid)
            if new_grid != grid:
                gl.add_new_tile(new_grid)
                grid = new_grid
                if gl.check_game_over(grid):
                    gl.print_grid(grid)
                    print("Game Over! No more moves available.")
                    game_over = True
            else:
                print("Move not possible. Try a different direction.")
        else:
            print("Invalid move. Use w (up), a (left), s (down), or d (right)")

if __name__ == '__main__':
    #app.run(debug=True)
    main()