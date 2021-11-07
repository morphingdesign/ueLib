// -----------------------------------------------------------
// NewActor.cpp
// v.1.0
// Updated: 20211107
// -----------------------------------------------------------

#include "NewActor.h"

// Sets default values
ANewActor::ANewActor()
{
    // Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
    PrimaryActorTick.bCanEverTick = true;

}

void ANewActor::OnConstruction()
{
    //ZTestFuncC();
}

// Called when the game starts or when spawned
void ANewActor::BeginPlay()
{
    Super::BeginPlay();

}

void ANewActor::PostRegisterAllComponents()
{
    ZTestFuncC();
    UE_LOG(LogTemp, Warning, TEXT("Post register all components."));

}

// Called every frame
void ANewActor::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

}

// ZTestFuncA
// Convert static mesh components to HISMs, including registering and parenting.
void ANewActor::ZTestFuncA(UHierarchicalInstancedStaticMeshComponent*& NewHISM, FName Name)
{
    UHierarchicalInstancedStaticMeshComponent* HISM;
    NewHISM = NewObject<UHierarchicalInstancedStaticMeshComponent>(this, HISM->StaticClass(), Name);
    NewHISM->SetupAttachment(RootComponent);
    NewHISM->RegisterComponent();
    AddInstanceComponent(NewHISM);
    NewHISM->SetFlags(RF_Transactional);
}

// ZTestFuncC
// Intended to clear static meshes when enabled by user.
void ANewActor::ZTestFuncC()
{
    if (clearStaticMeshes)
    {
        UE_LOG(LogTemp, Warning, TEXT("Clear Static Meshes is enabled."));
    }
    // Filter all components in actor to collect only static
    // meshes. Verify no HISM (child class) are included.
    // Detach from actor.
    // Destroy actors.

    TArray<UStaticMeshComponent*> StaticComps;
    GetComponents<UStaticMeshComponent>(StaticComps);

    //for (UStaticMeshComponent StComp : StaticComps)
    //{
    //	FString Name = GetName(StComp);
    //	UE_LOG(LogTemp, Warning, TEXT(Name));
    //}

    for (int32 i = 0; i < StaticComps.Num(); i++)
    {
        //AActor::GetName(StaticComps[i]).ToString();
        //UE_LOG(LogTemp, Warning, TEXT("test"));
        //UE_LOG(LogTemp, Warning, TEXT(StaticComps[i]->GetName.ToString()));
        // StaticComps[i]->GetName
    }
}