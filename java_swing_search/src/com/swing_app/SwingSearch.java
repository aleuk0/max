package com.swing_app;


// Java program to create a simple SwingSearch 
// with basic +, -, /, * using java swing elements 

import java.awt.event.*;
import javax.swing.*;
import java.awt.*;

class SwingSearch extends JFrame implements ActionListener {

    static JFrame frame;  // create a frame
    static JTextField textfield;  // create a textfield
    static JTextField n_field;  // create a n_field

    Integer a, b, n;  // class var

    SwingSearch() {  // default values
        a = 1000000;
        b = 1;
        n = 0;
    }

    // main function 
    public static void main(String args[]) {
        // create a frame 
        frame = new JFrame("SwingSearch");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        try {
            // set look and feel 
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        // create a object of class 
        SwingSearch s_search = new SwingSearch();

        // create a textfield 
        textfield = new JTextField(30);
        textfield.setEditable(false); // set the textfield to non editable

        n_field = new JTextField(15);
        n_field.setEditable(false);

        // create number buttons and some operators 
        JButton yes, no, new_guess, exit;

        // create number buttons 
        yes = new JButton("yes");
        no = new JButton("no");
        new_guess = new JButton("new guess");
        exit = new JButton("exit");

        // create a panel 
        JPanel j_panel = new JPanel();

        // add action listeners
        new_guess.addActionListener(s_search);
        yes.addActionListener(s_search);
        no.addActionListener(s_search);
        exit.addActionListener(s_search);

        // add elements to panel 
        j_panel.add(textfield);
        j_panel.add(new_guess);
        j_panel.add(yes);
        j_panel.add(no);
        j_panel.add(exit);
        j_panel.add(n_field);

        // set Background of panel 
        j_panel.setBackground(Color.blue);

        // add panel to frame 
        frame.add(j_panel);

        frame.setSize(500, 220);
        frame.show();
    }

    public void actionPerformed(ActionEvent e) {

        textfield.setText("Number <= " + (SwingSearch.round((a + b) / 2, 2)) + "?");

        String button_str = e.getActionCommand();

        if (button_str.equals("yes")) {
            a = (a + b) / 2;
            n += 1;
            if (Math.round(a) == (Math.round(b))) {
                textfield.setText("Your number is " + SwingSearch.round(a, 2));
                n_field.setText("Completed in " + n + " moves!");
            }

        } else if (button_str.equals("no")) {
            b = (a + b) / 2;
            n += 1;
            if (Math.round(a) == (Math.round(b))) {
                textfield.setText("Your number is " + SwingSearch.round(a, 2));
                n_field.setText("Completed in " + n + " moves!");
            }

        } else if (button_str.equals("new guess")) {
            a = 1000000;
            b = 1;
            textfield.setText("Guess numbers from 1 to 1000000. Number <= 500000?");

        } else if (button_str.equals("exit")) {
            textfield.setText("Exit");
            frame.dispatchEvent(new WindowEvent(frame, WindowEvent.WINDOW_CLOSING));
        }

        else {
            textfield.setText("You have a mistake in keyboard input. To exit enter \'exit\'");
        }
    }

    private static double round(double value, int places) {
        if (places < 0)
            throw new IllegalArgumentException();

        long factor = (long) Math.pow(10, places);
        value = value * factor;
        long tmp = Math.round(value);
        return (double) tmp / factor;
    }
} 
