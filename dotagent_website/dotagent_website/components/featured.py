import nextpy as xt


def featured():
    return xt.fragment(
        xt.box(
            xt.text(
                "Featured",
                class_name="lg:my-6 font-[DMSans] h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                xt.box(
                    xt.box(
                        xt.image(
                            src="/FeaturedCard1new.png",
                            class_name="w-full ",
                        ),
                    ),
                    xt.box(
                        xt.text(
                            "Most Powerful ChatGPT : Dot",
                            class_name="mb-1 font-bold tracking-tight md:text-2xl font-[DMSans] text-[1.3rem] leading-7 text-white",
                        ),
                        xt.box(
                            xt.text(
                                "Enterprise-grade security & privacy and the most powerful version of ChatGPT yet.",
                                class_name="font-normal text-[#C4C4C4] font-[DMSans] text-sm md:text-base max-w-md",
                            ),
                            xt.box(
                                "FREE",
                                class_name="bg-[#8E55EA] text-white px-8 py-2 font-[DMSans] tracking-normal rounded-full",
                            ),
                            class_name="flex justify-between space-x-2 items-center",
                        ),
                        class_name="px-5  py-4 ",
                    ),
                    class_name="bg-[#4e3579] rounded-b-3xl rounded-t-[2.5rem] ",
                ),
                xt.box(
                    xt.image(
                        src="/FeaturedCard2.png",
                        class_name="w-full ",
                    ),
                    xt.box(
                        xt.box(
                            xt.box(
                                xt.box(
                                    xt.image(
                                        src="/MobileLegends.png",
                                        class_name="w-20 h-20  ",
                                    ),
                                ),
                                xt.box(
                                    xt.text(
                                        "Mobile Leggends: Bang Bag",
                                        class_name="text-xl font-[DMSans] text-white my-2 sm:leading-5",
                                    ),
                                    xt.text(
                                        "Enterprise-grade security & privacy and the most powerful version of ChatGPT yet.",
                                        class_name="text-xs max-w-md text-white font-[DMSans] ",
                                    ),
                                    class_name="flex flex-col",
                                ),
                                class_name="flex items-center gap-6",
                            ),
                            xt.box(
                                xt.text(
                                    "$11",
                                    class_name="text-[#F29586] line-through font-[DMSans] text-center",
                                ),
                                xt.box(
                                    "$1",
                                    class_name="bg-gradient-to-b h-11 w-20 from-green-500 to-green-700 rounded-full text-white flex items-center font-Poppins justify-center",
                                ),
                                class_name="flex items-center  gap-4",
                            ),
                            class_name="flex items-center justify-between gap-6 pt-6",
                        ),
                        xt.box(
                            xt.box(
                                xt.box(
                                    xt.image(
                                        src="/MobileLegends.png",
                                        class_name="w-20 h-20  ",
                                    ),
                                ),
                                xt.box(
                                    xt.text(
                                        "Mobile Leggends: Bang Bag",
                                        class_name="text-xl font-[DMSans] text-white my-2 sm:leading-5",
                                    ),
                                    xt.text(
                                        "Enterprise-grade security & privacy and the most powerful version of ChatGPT yet.",
                                        class_name="text-xs max-w-md text-white font-[DMSans] ",
                                    ),
                                    class_name="flex flex-col",
                                ),
                                class_name="flex items-center gap-6",
                            ),
                            xt.box(
                                xt.text(
                                    "$11",
                                    class_name="text-[#F29586] line-through font-[DMSans] text-center",
                                ),
                                xt.box(
                                    "$1",
                                    class_name="bg-gradient-to-b h-11 w-20 from-green-500 to-green-700 rounded-full text-white flex items-center font-Poppins justify-center",
                                ),
                                class_name="flex items-center  gap-4",
                            ),
                            class_name="flex items-center justify-between gap-6 pt-6",
                        ),
                        class_name=" px-5 py-6 ",
                    ),
                    class_name="bg-[#101213] rounded-b-3xl rounded-t-[2.5rem] ",
                ),
                class_name="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2  gap-10  w-full",
            ),
        ),
    )
