package com.muhammedalikocabey.try_mvmm_kotlin.ui.quotes


import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import com.muhammedalikocabey.try_mvmm_kotlin.data.Quote
import com.muhammedalikocabey.try_mvmm_kotlin.databinding.ActivityQuotesBinding
import com.muhammedalikocabey.try_mvmm_kotlin.utilities.InjectorUtils

class QuotesActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuotesBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuotesBinding.inflate(layoutInflater)
        setContentView(binding.root)

        initializeUI()
    }

    private fun initializeUI() {
        val factory = InjectorUtils.provideQuotesViewModelFactory()
        val viewModel = ViewModelProviders.of(this, factory)
            .get(QuotesViewModel::class.java)

        viewModel.getQuotes().observe(this, Observer { quotes ->
            val stringBuilder = StringBuilder()
            quotes.forEach{ quote ->
                stringBuilder.append("$quote\n\n")
            }
            binding.textViewQuotes.text = stringBuilder.toString()
        })

        binding.buttonAddQuote.setOnClickListener {
            val quote = Quote(binding.editTextQuote.text.toString(), binding.editTextAuthor.text.toString())
            viewModel.addQuote(quote)
            binding.editTextQuote.setText("")
            binding.editTextAuthor.setText("")
        }


    }
}