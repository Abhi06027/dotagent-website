import nextpy as xt


def Interviewprep_img(src):
    return xt.box(
        xt.box(
            xt.box(
                xt.box(
                    xt.image(
                        src=src,
                        class_name="lg:w-80 lg:h-80 md:w-80 w-72 relative text-lg rounded-t-lg font-semibold text-[#6c7275] bg-[rgba(20,_23,_24,_0.5)] self-start",
                    ),
                    xt.box(
                        xt.text(
                            "Interview Prep",
                            class_name="md:text-sm text-xs text-white shadow-[0px_25px_39px_-20px_rgba(15,15,_15,_0.1)] bg-[linear-gradient(93deg,#23262f_0%,rgba(35,_38,_47,_0.7)_0%)] bg-cover bg-no-repeat flex flex-col items-center ml-0 px-2 py-1 rounded-full ",
                        ),
                        xt.text(
                            "Figma",
                            class_name="text-3xl font-inter font-bold tracking-[-1.28] leading-[3rem] text-white ",
                        ),
                        class_name="absolute pl-5 py-3 top-0 left-0",
                    ),
                    class_name="relative",
                ),
            ),
            xt.box(
                xt.box(
                    xt.image(
                        src="/Frame.png",
                        class_name="w-11 h-11",
                    ),
                    xt.box(
                        xt.box(
                            xt.text(
                                "Duolingo",
                                class_name="md:text-sm text-xs  font-medium text-[#fefefe] leading-6",
                            ),
                            xt.text(
                                "Language learning app",
                                class_name="text-[0.65rem] md:text-xs  font-medium leading-4 text-[#6c7275]",
                            ),
                            class_name="flex flex-col",
                        ),
                        xt.box(
                            xt.box(
                                xt.text(
                                    "FREE",
                                    class_name="text-[0.813rem] font-[Poppins] font-extrabold  tracking-[0.36] bg-clip-text text-transparent bg-gradient-to-r from-[#00C4CC] via-[#0FD1B6] to-[#2AE88D]",
                                ),
                                xt.text(
                                    "$20",
                                    class_name="text-xs line-through  tracking-[0.36] text-[#ee806f]",
                                ),
                            ),
                            class_name="bg-[#343839] text-xs tracking-[0.36] text-[#E8ECEF] flex flex-col justify-center items-center text-center h-10 px-6 py-6  rounded-3xl",
                        ),
                        class_name="flex space-x-4 items-center ",
                    ),
                    class_name="bg-[#1b1e1f] lg:w-full md:w-80 w-72 flex gap-4 p-4 rounded-b-lg",
                ),
            ),
        ),
    )


def Interviewprep():
    return xt.fragment(
        xt.box(
            xt.text(
                "Interview prep apps",
                class_name="lg:my-6 font-[DMSans] h6 lg:text-2xl my-2 text-lg md:my-4 md:text-[1.375rem] leading-8 text-[#E8ECEF] font-normal",
            ),
            xt.box(
                Interviewprep_img("/you-image.jpg"),
                Interviewprep_img("/Image2.jpg"),
                Interviewprep_img("/Image3.jpg"),
                Interviewprep_img("/Image4.jpg"),
                Interviewprep_img("/you-image.jpg"),
                class_name="flex space-x-2 whitespace-nowrap overflow-x-scroll lg:overflow-x-hidden gap-4",
            ),
        ),
    )
