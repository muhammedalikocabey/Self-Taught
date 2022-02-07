package com.muhammedalikocabey.try_mvmm_kotlin.ui.quotes

import androidx.lifecycle.ViewModel
import com.muhammedalikocabey.try_mvmm_kotlin.data.Quote
import com.muhammedalikocabey.try_mvmm_kotlin.data.QuoteRepository


class QuotesViewModel(private val quoteRepository: QuoteRepository) : ViewModel() {

    fun getQuotes() = quoteRepository.getQuotes()

    fun addQuote(quote: Quote) = quoteRepository.addQuote(quote)


}