//
//  ViewController.swift
//  Calculator
//
//  Created by Muhammed Ali Kocabey on 21.12.2021.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var number1TextView: UITextField!
    
    @IBOutlet weak var number2TextView: UITextField!
    
    @IBOutlet weak var resultLabel: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func additionClicked(_ sender: Any) {
        
        if let firstNumber = Double(number1TextView.text!) {
            
            if let secondNumber = Double(number2TextView.text!) {
                
                let Result = firstNumber + secondNumber
                
                resultLabel.text = "Result :  " + String(Result)
            } else {
                resultLabel.text = "Please enter numbers instead of text."
            }
            
        } else {
            resultLabel.text = "Please enter numbers instead of text."
        }
    }
    
    
    @IBAction func minusClicked(_ sender: Any) {
        
        if let firstNumber = Double(number1TextView.text!) {
            
            if let secondNumber = Double(number2TextView.text!) {
                
                let Result = firstNumber - secondNumber
                
                resultLabel.text = "Result :  " + String(Result)
            } else {
                resultLabel.text = "Please enter numbers instead of text."
            }
            
        } else {
            resultLabel.text = "Please enter numbers instead of text."
        }

    }
    
    @IBAction func multiplicationClicked(_ sender: Any) {
        
        if let firstNumber = Double(number1TextView.text!) {
            
            if let secondNumber = Double(number2TextView.text!) {
                
                let Result = firstNumber * secondNumber
                
                resultLabel.text = "Result :  " + String(Result)
            } else {
                resultLabel.text = "Please enter numbers instead of text."
            }
            
        } else {
            resultLabel.text = "Please enter numbers instead of text."
        }
        
    }
    
    @IBAction func divisionClicked(_ sender: Any) {
        
        if let firstNumber = Double(number1TextView.text!) {
            
            if let secondNumber = Double(number2TextView.text!) {
                
                let Result = firstNumber / secondNumber
                
                resultLabel.text = "Result :  " + String(Result)
            } else {
                resultLabel.text = "Please enter numbers instead of text."
            }
            
        } else {
            resultLabel.text = "Please enter numbers instead of text."
        }
        
    }
}

