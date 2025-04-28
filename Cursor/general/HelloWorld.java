package Cursor.general;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class HelloWorld {
    public static void main(String[] args) {
        // Crear la ventana principal
        JFrame frame = new JFrame("Mi Primera Interfaz");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLayout(new FlowLayout());

        // Crear los componentes
        JLabel label = new JLabel("Ingrese su nombre:");
        JTextField textField = new JTextField(20);
        JButton button = new JButton("Saludar");
        JLabel resultado = new JLabel("");

        // Agregar acción al botón
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String nombre = textField.getText();
                resultado.setText("¡Hola " + nombre + "!");
            }
        });

        // Agregar componentes a la ventana
        frame.add(label);
        frame.add(textField);
        frame.add(button);
        frame.add(resultado);

        // Mostrar la ventana
        frame.setVisible(true);
    }
}
        
